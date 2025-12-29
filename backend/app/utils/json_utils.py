# app/utils/json_utils.py
import json
import re

def extract_json(text: str) -> dict:
    """
    Safely extracts JSON from LLM output.
    Handles:
    - Markdown ```json blocks
    - Extra text before/after JSON
    - Invalid or empty responses
    """

    if not text or not text.strip():
        return {}

    # Try direct JSON first
    try:
        return json.loads(text)
    except Exception:
        pass

    # Extract JSON inside ```json ``` blocks
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            return {}

    # Extract first {...} block
    match = re.search(r"(\{.*\})", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except Exception:
            return {}

    return {}
