import requests
import re


class ContentAgent:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"

    def generate_content(self, user_input, tone="expert"):

        prompt = f"""
Generate EXACTLY 5 LinkedIn posts.

Goal:
{user_input}

Tone: {tone}

STRICT RULES:
- DO NOT write "Post 1", "Post 2"
- DO NOT number posts
- DO NOT add intro text
- Each post must be full paragraph
- Separate ONLY with ###

Output:
content
###
content
"""

        payload = {
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 250
            }
        }

        try:
            response = requests.post(self.url, json=payload)

            if response.status_code != 200:
                return ["❌ Ollama API error"]

            raw_output = response.json().get("response", "").strip()

            # -------------------------------
            # 🔥 SPLIT
            # -------------------------------
            posts = raw_output.split("###")

            if len(posts) <= 1:
                posts = re.split(r"\n\s*\d+\.\s+", raw_output)

            # -------------------------------
            # 🔥 CLEAN
            # -------------------------------
            clean_posts = []

            for p in posts:
                p = p.strip()

                # ❌ Remove empty or junk
                if not p or len(p) < 30:
                    continue

                # ❌ Remove "Post X"
                if re.fullmatch(r"post\s*\d+", p.lower()):
                    continue

                # ❌ Remove intro
                if "here are" in p.lower():
                    continue

                # ❌ Remove "Post X:"
                if p.lower().startswith("post"):
                    parts = p.split(":", 1)
                    if len(parts) > 1:
                        p = parts[1].strip()

                # ❌ Remove numbering
                p = re.sub(r"^\d+\.\s*", "", p)

                clean_posts.append(p)

            if not clean_posts:
                return ["❌ No content generated"]

            return clean_posts[:5]

        except Exception as e:
            return [f"❌ Ollama error: {e}"]