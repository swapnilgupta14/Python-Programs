import os
import random
print(os.listdir("C:/"))
# it will print all the folders names as an array in the C directory

print("\nSelect a random file from a given directory")
print(random.choice(os.listdir("C:/")))
# to print random name of one folder in the c directory
# here slash C:/ is fucking important

