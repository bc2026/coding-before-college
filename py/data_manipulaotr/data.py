import csv

f = open('data.csv', 'r')
Lines = f.readlines()

intr = 0 # integer value for right
intl = 0 # integer value for left
fr = 0 # decimal value for right
fl = 0 # decimal value for left
sigma0 = 0 # sum of intr/intl + fr/fl
sigma1 = 0
valuesR = []
valuesL = []
print("valueL, valueR")
for line in Lines:
    split = line.split(",")
    try:
        rightn = split[0]
        leftn = split[1]

        intr = rightn[1:rightn.find("/")-2]
        fr = rightn[rightn.find("/")-2:]
        intl = leftn[1:leftn.find("/")-2]
        fl = leftn[rightn.find("/")-2:]
        fl = fl[0:fl.find('"')]
        
        dr = int(fr[:fr.find("/")])/int(fr[fr.find("/")+1:])
        dl = int(fl[:fl.find("/")])/int(fl[fl.find("/")+1:])
        
        sigma0 = int(intr) + dr
        sigma1 = int(intl) + dl
        
        print(str(sigma1) + ", " + str(sigma0))
        
        
    except IndexError:
        pass

