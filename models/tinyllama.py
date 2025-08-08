import requests

def ask_tinyllama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        result = res.json()
        return result.get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {e}"
