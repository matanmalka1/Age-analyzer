import requests

def get_data_with_headers(name: str):
    url = f"https://api.agify.io?name={name}"
    headers = {
        "User-Agent": "MatanBot/1.0",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as err:
        print(f"HTML error occurred: {err}")
        return None

# print(get_data_with_headers("matan"))