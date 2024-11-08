import requests

api_key = "Bearer sk-QICSb4M1LkpgHOTK30NzlzuJ22ppCslppoOOoKd12H5CPP10"


# Get the user's prompt
def get_prompt_from_user():
    # other thing
    # ...
    return """爱沙尼亚历史"""


def main():
    # Before starting a session, you need to create a thread first
    url = "https://api.deepbricks.ai/api/v1/threads"
    resp = requests.post(url, headers={"Authorization": "Bearer sk-QICSb4M1LkpgHOTK30NzlzuJ22ppCslppoOOoKd12H5CPP10"})
    thread = resp.json()
    if resp.status_code != 200:
        print(resp.json())
        return

    # multi turn chat
    while True:
        # 1. create message
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/messages"
        body = {
            "role": "user",
            "content": get_prompt_from_user()
        }
        resp = requests.post(url, headers={"Authorization": api_key}, json=body)
        if resp.status_code != 200:
            print(resp.json())
            return

        # 2. create run
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/runs"
        body = {
            "model": "gpt-3.5-turbo"
        }
        resp = requests.post(url, headers={"Authorization": api_key}, json=body)
        run = resp.json()
        if resp.status_code != 200:
            print(resp.json())
            return

        # 3. get assistant answer
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/messages?run_id={run['id']}"
        resp = requests.get(url, headers={"Authorization": api_key})
        print(resp.json())


if __name__ == '__main__':
    main()
