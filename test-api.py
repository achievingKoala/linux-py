import requests

url = "https://api.deepbricks.ai/v1/chat/completions"
body = {
    "model": "gpt-4o-2024-08-06",
    "messages": [
        {
            "role": "user",
            "content": """Hello!"""
        }
    ],
    "stream": True
}
response = requests.post(url, headers={"Authorization": "Bearer sk-QICSb4M1LkpgHOTK30NzlzuJ22ppCslppoOOoKd12H5CPP10"}, json=body, stream=True)
for chunk in response.iter_lines():
    print(chunk)