import os
from os import path

hwnum = str(3)
user = "INSERT COMMAND LINE OUTPUT USER HERE"
command = "INSERT PATH HERE"
os.chdir(command)

i = 1
while (path.isfile('p' + str(i) + ".mypl")):
    command = "java HW" + hwnum + " p" + str(i) + ".mypl"
    print(user, command)
    os.system(command)
    i += 1

i = 1
while (path.isfile('e' + str(i) + ".mypl")):
    command = "java HW" + hwnum + " e" + str(i) + ".mypl"
    print(user, command)
    os.system(command)
    i += 1
