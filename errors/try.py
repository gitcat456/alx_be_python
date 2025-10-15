import requests

def get_github_user_info():
    username = input("Enter GitHub username: ").strip()

    if not username:
        print("Error: Username cannot be empty.")
        return

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)  # Added timeout to avoid hanging
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Error: GitHub user not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return
    except requests.exceptions.ConnectionError:
        print("Error: Network connection error.")
        return
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
        return
    except requests.exceptions.RequestException as err:
        print(f"An error occurred while making the request: {err}")
        return

    try:
        data = response.json()
    except ValueError:
        print("Error: Response content is not valid JSON.")
        return

    try:
        for key, value in data.items():
            print(f"{key}: {value}")

        login = data.get('login', 'Unknown user')
        public_repos = data.get('public_repos', 'Unknown')
        print(f"{login} has {public_repos} public repos.")
    except (KeyError, TypeError) as e:
        print(f"Error: Unexpected data structure in response. {e}")

if __name__ == "__main__":
    get_github_user_info()
