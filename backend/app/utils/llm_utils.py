import json
import re
from typing import Optional

def extract_json(response: str) -> Optional[dict]:
    """
    Extract JSON from LLM response even if wrapped in backticks or has extra text.
    Returns None if parsing fails.
    """
    if not response:
        return None

    # Remove backticks and optional 'json'
    cleaned = re.sub(r"^```(json)?|```$", "", response.strip(), flags=re.I).strip()

    # Find first JSON object in string
    match = re.search(r"{.*}", cleaned, flags=re.S)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return None
    return None
