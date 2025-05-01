import requests

def summarize_paper(paper, pdf_text):
    """
    Summarize the paper using Ollama (Gemma 3B)
    """
    url = "http://172.20.0.1:11434/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }

    prompt = (
        f"You are an academic assistant. Summarize the following paper in clear, concise points. Do not Exceed 500 words.\n\n"
        f"Title: {paper['title']}\n\n"
        f"Content:\n{pdf_text}\n\n"
        f"Summary:"
    )

    payload = {
        "model": "gemma3:1b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except KeyError:
        print("Unexpected response format:", response.json())
        return None
