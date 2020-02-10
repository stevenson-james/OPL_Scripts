import os
from os import path

command = "INSERT PATH HERE"
os.chdir(command)

of = open("combinedTests.txt", "w+")

#change pVal to YOUR first p test case 
pVal = 8
while (path.isfile('p' + str(pVal) + '.mypl')):
    f = open('p' + str(pVal) + '.mypl', 'r')
    of.write('----------p' + str(pVal) + '.mypl----------\n')
    f1 = f.readlines()
    for x in f1:
        of.write(x)
    of.write('\n\n')
    pVal += 1

#change eVal to YOUR first e test case 
eVal = 1
while (path.isfile('e' + str(eVal) + '.mypl')):
    of.write('\n\n')
    f = open('e' + str(eVal) + '.mypl', 'r')
    of.write('----------e' + str(eVal) + '.mypl----------\n')
    f1 = f.readlines()
    for x in f1:
        of.write(x)
    eVal += 1

