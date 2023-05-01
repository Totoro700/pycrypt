import os, time, sys, string

def fileCheck(fn):
    return os.path.isfile(fn)

def writeOutput(str: list):
    f = open('output.txt', 'w')
    f.write(str)
    f.close()

def switch(str: list, alph: list):
    strLen = len(str)
    a = 0
    temp = []
    print(strLen)
    while a < strLen:
        if str[a] == string.punctuation || str[a] == " ":
            
        toAppend = alph[]
        temp.append(toAppend)
        a=a+1
        print(a)
    return ''.join(temp)
    #make array of numbers into letters and return

def crypt(str: list):
    crypted = []
    alph = list(string.ascii_letters + string.digits + string.punctuation + " ")
    temp = []
    cryptedNums = []
    for i in str:
        temp.append(alph.index(i))
    cryptedNums = [x+1 for x in temp]
    crypted = switch(cryptedNums, alph)
    writeOutput(crypted)

def loop():
    filename = input('File name (exact directory like "example.txt") ')
    if fileCheck(filename):
        file = open(filename, 'r')
        print(crypt(list(file.read())))
        file.close()
    else:
        print('Invalid file name try again')

while True:
    loop()