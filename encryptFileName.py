import encrypt
import os

word = "hellfire"
letters = []
decrypt = []
path = "C:\Users\Atarimaster\Desktop\Code\Python\decrypt"

action = raw_input("Would you like to encrypt(e) or decrypt(d) files?: ")

if action == "e":
    for l in word:
        letters.append(l)

    encrypt.encryptWord(letters)

elif action == "d":
    dirList = os.listdir(path)

    for fname in dirList:
        decrypt.append(fname)

        encrypt.decryptWord(decrypt)

else:
    print "Please enter E or D"
