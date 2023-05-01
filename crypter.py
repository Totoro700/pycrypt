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
    alph = alph.append(" ")
    while a < strLen: #idfk what's going on here
        """try: 
            temp.append(alph[str[a]])
            a=a+1
        except TypeError: 
            temp.append("a")
            a=a+1"""
        temp.append(alph[str[a]])
        a=a+1
        #print(a)
    print(''.join(temp))
    return ''.join(temp)
    #make array of numbers into letters and return

def crypt(str: list):
    crypted = []
    alph = list(string.ascii_letters + string.digits + string.punctuation + " " + string.whitespace)
    temp = []
    cryptedNums = []
    for i in str:
        temp.append(alph.index(i))
    cryptedNums = [x+18 for x in temp]
    #print(cryptedNums)
    writeOutput(switch(cryptedNums, alph))

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