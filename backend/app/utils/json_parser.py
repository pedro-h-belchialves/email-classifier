import json
import re


def extract_json(text: str) -> dict:
    try:
        return json.loads(text)

    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

    raise ValueError("Não foi possível converter a resposta da IA em JSON")