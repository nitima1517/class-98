from fileinput import filename


def counting():
    fileName= open("sample.txt",'r')
   # print(fileName.read())
    numberOfWOrds=0
    for line in fileName:
        words=line.split()
        numberOfWOrds=numberOfWOrds+len(words)
    print(numberOfWOrds)        
counting()