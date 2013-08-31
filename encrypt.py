import os

def encryptWord(letterList):
    encrypted = []
    final = ""
    
    for letter in letterList:
        if letter == "a":
            encrypted.append(69)
        if letter == "b":
            encrypted.append(71)
        if letter == "c":
            encrypted.append(66)
        if letter == "d":
            encrypted.append(13)
        if letter == "e":
            encrypted.append(56)
        if letter == "f":
            encrypted.append(91)
        if letter == "g":
            encrypted.append(54)
        if letter == "h":
            encrypted.append(35)
        if letter == "i":
            encrypted.append(18)
        if letter == "j":
            encrypted.append(12)
        if letter == "k":
            encrypted.append(25)
        if letter == "l":
            encrypted.append(19)
        if letter == "m":
            encrypted.append(12)
        if letter == "n":
            encrypted.append(11)
        if letter == "o":
            encrypted.append(17)
        if letter == "p":
            encrypted.append(16)
        if letter == "q":
            encrypted.append(30)
        if letter == "r":
            encrypted.append(40)
        if letter == "s":
            encrypted.append(82)
        if letter == "t":
            encrypted.append(21)
        if letter == "u":
            encrypted.append(95)
        if letter == "v":
            encrypted.append(79)
        if letter == "w":
            encrypted.append(10)
        if letter == "x":
            encrypted.append(22)
        if letter == "y":
            encrypted.append(97)
        if letter == "z":
            encrypted.append(84)

    for num in encrypted:
        final += str(num)

    print final
        

def decryptWord(decrypt):
    dnumbers = []
    orig = []
    origName = ""
    nameLen = []
    finalName = []
    path = "C:\Users\Atarimaster\Desktop\Code\Python\decrypt"
    oldNames = os.listdir(path)
    
    for fname in decrypt:
        i = 0
        x = 2
        length = len(fname)
        nameLen.append(length)

        while x <= length:
            num = fname[i:x]
            dnumbers.append(int(num))
            x += 2
            i += 2
    
    for n in dnumbers:
        if n == 69:
            orig.append("a")
        if n == 71:
            orig.append("b")
        if n == 66:
            orig.append("c")
        if n == 13:
            orig.append("d")
        if n == 56:
            orig.append("e")
        if n == 91:
            orig.append("f")
        if n == 54:
            orig.append("g")
        if n == 35:
            orig.append("h")
        if n == 18:
            orig.append("i")
        if n == 12:
            orig.append("j")
        if n == 25:
            orig.append("k")
        if n == 19:
            orig.append("l")
        if n == 12:
            orig.append("m")
        if n == 11:
            orig.append("n")
        if n == 17:
            orig.append("o")
        if n == 16:
            orig.append("p")
        if n == 30:
            orig.append("q")
        if n == 40:
            orig.append("r")
        if n == 82:
            orig.append("s")
        if n == 21:
            orig.append("t")
        if n == 95:
            orig.append("u")
        if n == 79:
            orig.append("v")
        if n == 10:
            orig.append("w")
        if n == 22:
            orig.append("x")
        if n == 97:
            orig.append("y")
        if n == 84:
            orig.append("z")

    for letter in orig:
        origName += letter
       
    j = 0
    start = 0
    while (j < len(nameLen)):
        end = start + (nameLen[j] / 2)
        finalName.append(origName[start:end])
        start = end
        j = j + 1
        
    k = 0
    for f in finalName:
        os.rename(os.path.join(path, oldNames[k]),os.path.join(path,finalName[k]))
        k = k + 1
        
        
        


   
            

            
        
        
        












        
    
