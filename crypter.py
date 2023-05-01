import os, time, sys, string

def t(msg):
    for i in msg:
        sys.stdout.flush()
        sys.stdout.write(i)
        time.sleep(0.02)
    print()
           

def fileCheck(fn):
    return os.path.isfile(fn)

def writeOutput(str: list):
    f = open('output.txt', 'w')
    open.write(str)
    f.close()


def crypt(str: list):
    crypted = []
    alph = list(string.ascii_letters)
    for i in str:
                

def loop():
    filename = input('File name (exact directory like "example.txt") ')
    if fileCheck(filename):
        file = open(filename, 'r')
        t(crypt(list(file.read())))
        file.close()
    else:
        t('Invalid file name try again')

while True:
    loop()