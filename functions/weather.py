import requests

username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    for key, value in data.items():
        print(f"{key}: {value}")
    print(f"{data['login']} has {data['public_repos']} public repos.")
else:
    print("User not found.")
