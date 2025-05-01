import requests

def generate_flashcards(text):
    """
    Use Ollama to generate flashcards in Markdown format.
    """
    url = "http://172.20.0.1:11434/v1/chat/completions"  # Docker DNS
    headers = {"Content-Type": "application/json"}

    prompt = (
        "You are a helpful academic tutor. Based on the following text, generate concise and useful flashcards "
        "in Markdown format with the format:\n\n"
        "**Q: ...**\n**A: ...**\n\n"
        "Use bullet points or separate sections. Ensure the flashcards focus on key definitions, concepts, and ideas.\n\n"
        f"Text:\n{text}\n\nFlashcards:"
    )

    payload = {
        "model": "gemma3:1b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 1000,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Flashcard request failed: {e}")
        return None
    except KeyError:
        print("Unexpected response format:", response.json())
        return None

