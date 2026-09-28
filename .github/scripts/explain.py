#!/usr/bin/env python3
"""
GitHub Actions Cloud Explanation Generator
============================================
Runs directly inside GitHub Actions whenever a solution is committed.
Uses Google Gemini 3.8 Flash to write a crystal-clear, deep, mathematically
rigorous explanation and writes README.md directly to the repository.
"""

import os
import sys
import json
import time
import re
from pathlib import Path
import httpx

SYSTEM_PROMPT = """You are an elite algorithms professor, competitive programming champion, and rigorous technical writer.
Your ONLY responsibility is to explain the user's EXACT submitted code retrieved from their repository.

CRITICAL INSTRUCTIONS:
1. Explain ONLY the submitted code.
2. Do NOT replace the algorithm with a different or more optimal one.
3. Do NOT generate an alternative solution.
4. Follow the actual control flow and variable names of the submitted implementation.
5. Every algorithmic claim must correspond directly to the submitted code.
6. Derive time complexity mathematically from the actual implementation.
7. Derive space complexity from the actual auxiliary memory used.
8. Do NOT invent variables, data structures, loops, conditions, or operations that do not exist.
9. Output must be formatted in clean GitHub Markdown matching this exact structure:

# [Problem Title]

## Problem
[Concise summary of the problem requirements]

## Approach
[Clear explanation of the approach used in the submitted code]

## How the Solution Works
[Detailed walkthrough referencing the exact variables and flow in the code]

## Algorithm
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Why This Works
[Theoretical correctness justification]

## Complexity
### Time Complexity
`[e.g. O(n) or O(n³)]` — [Detailed arithmetic justification]

### Space Complexity
`[e.g. O(1) or O(n)]` — [Detailed memory justification]

## Edge Cases
- [Edge case 1]
- [Edge case 2]

## Solution
```[language]
[Exact submitted code]
```
"""

def enforce_exact_solution(ai_text: str, problem_number: int, problem_title: str, language: str, code: str) -> str:
    text = ai_text.strip()
    expected_heading = f"# {problem_number}. {problem_title}"
    lines = text.split("\n")
    if lines and lines[0].startswith("#"):
        lines[0] = expected_heading
        text = "\n".join(lines)
    else:
        text = f"{expected_heading}\n\n" + text

    sol_idx = text.rfind("## Solution")
    if sol_idx != -1:
        text = text[:sol_idx].rstrip()

    text = text + f"\n\n## Solution\n\n```{language}\n{code.strip()}\n```\n"
    return text

def call_gemini(api_key: str, prompt: str) -> str:
    models = ["gemini-3.8-flash", "gemini-3.5-flash", "gemini-flash-latest"]
    for model_name in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        body = {
            "contents": [{"parts": [{"text": f"{SYSTEM_PROMPT}\n\n{prompt}"}]}]
        }
        for attempt in range(3):
            try:
                with httpx.Client(timeout=60.0) as client:
                    res = client.post(url, json=body)
                    if res.status_code == 200:
                        data = res.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            if parts and "text" in parts[0]:
                                return parts[0]["text"]
                    elif res.status_code in (503, 429):
                        time.sleep(2 * (attempt + 1))
                        continue
                    else:
                        break
            except Exception:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
    raise RuntimeError("Failed to generate explanation across all Gemini models.")

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY is not set in environment!")
        sys.exit(1)

    repo_root = Path(__file__).resolve().parent.parent.parent
    print(f"[*] Scanning repository root: {repo_root}")

    # Find problem folders matching e.g. '0020-valid-parentheses'
    problem_folders = [
        d for d in repo_root.iterdir()
        if d.is_dir() and re.match(r"^\d{4}-", d.name)
    ]
    problem_folders.sort(key=lambda d: d.name)
    print(f"[*] Found {len(problem_folders)} problem folder(s).")

    changed_count = 0

    for folder in problem_folders:
        folder_name = folder.name
        # Find solution file
        sol_file = next((f for f in folder.iterdir() if f.is_file() and f.name.startswith("solution.")), None)
        if not sol_file:
            continue

        readme_file = folder / "README.md"
        # Check if already generated
        if readme_file.exists():
            content = readme_file.read_text(encoding="utf-8", errors="replace")
            if len(content) > 1200 and "## Why This Works" in content:
                # Up to date
                continue

        print(f"\n--> Generating AI Explanation for {folder_name}...")
        sol_code = sol_file.read_text(encoding="utf-8", errors="replace").strip()
        prob_desc_file = folder / "problem.md"
        prob_desc = prob_desc_file.read_text(encoding="utf-8", errors="replace").strip() if prob_desc_file.exists() else ""

        # Parse number and title
        parts = folder_name.split("-", 1)
        prob_num = int(parts[0])
        prob_title = parts[1].replace("-", " ").title()

        # Check metadata.json
        meta_file = folder / "metadata.json"
        meta = {}
        if meta_file.exists():
            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8", errors="replace"))
                if meta.get("title"):
                    prob_title = meta["title"]
                if meta.get("problem_id"):
                    prob_num = int(meta["problem_id"])
            except Exception:
                pass

        lang = sol_file.suffix.lstrip(".")
        lang_map = {"cpp": "cpp", "py": "python", "java": "java", "js": "javascript", "ts": "typescript", "go": "go", "rs": "rust"}
        language = lang_map.get(lang, "cpp")

        user_prompt = f"Problem #{prob_num}: {prob_title}\nLanguage: {language}\n"
        if prob_desc:
            user_prompt += f"\nProblem Description:\n{prob_desc}\n"
        user_prompt += f"\nSubmitted Source Code:\n```{language}\n{sol_code}\n```\n"

        try:
            start_t = time.time()
            ai_text = call_gemini(api_key, user_prompt)
            final_md = enforce_exact_solution(ai_text, prob_num, prob_title, language, sol_code)
            readme_file.write_text(final_md, encoding="utf-8")
            elapsed = time.time() - start_t
            print(f"    [DONE] Written README.md in {elapsed:.2f}s ({len(final_md)} chars).")

            # Update metadata.json
            if meta_file.exists():
                meta["explanation_status"] = "ready"
                meta["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")

            changed_count += 1
        except Exception as e:
            print(f"    [ERROR] Failed to generate for {folder_name}: {e}")

    print(f"\n[*] Finished. Generated {changed_count} new explanation(s).")
    if changed_count > 0:
        # Signal to GitHub Actions that files changed
        with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
            f.write("has_changes=true\n")
    else:
        with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
            f.write("has_changes=false\n")

if __name__ == "__main__":
    main()
