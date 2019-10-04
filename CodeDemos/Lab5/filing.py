import os

path_of_execution = os.getcwd()

print("~"*30)
print("Current location where python program is running: ")
print("\t" + path_of_execution)

someFile = open("CodeDemos/Lab5/blank.txt", "r")

contents = someFile.read().split(" ")

someFile.close()

for i in contents:
    print(i)