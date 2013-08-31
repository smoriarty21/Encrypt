import os

files = []
convert = []
path="C:\Users\Atarimaster\Desktop\Code"

dirList=os.listdir(path)

for fname in dirList:
    files.append(fname)

for x in files:
    ext = x.endswith("3gp")

    if ext == True:
        convert.append(x)

for filename in convert:
    os.rename(filename, "test")
    
