import os

os.mkdir("PSIT")
print("New folder created successfully")
print("current location=",os.getcwd())

os.chdir("PSIT")
print("folder location changed. ")
print("current location=",os.getcwd())

os.mkdir("sub folder PSIT")
print("sub folder created")
print("current location=",os.getcwd())

os.chdir("sub folder PSIT")
print("Folder locatin changed again")
print("current location=",os.getcwd())

os.mkdir("second year")
print("Folder Created successfully")

os.mkdir("C:\\qwerty")
print("Folder Created in desited location")
