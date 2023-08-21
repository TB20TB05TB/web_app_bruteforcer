import requests

target_url = input("[*] Enter the target URL: ")
file_name = input("[*] Enter the file name, containing dirs: ")


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


file = open(file_name, "r")
for line in file:
    directory = line.strip()
    full_url = target_url + "/" + directory
    response = request(full_url)
    if response:
        print(f"[*] Discovered dir at this path: {full_url} ")
