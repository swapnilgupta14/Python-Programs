import os
os.mkdir("faltuu")
print("New folder created successfully")
os.chdir("faltuu")
print("folder location changed. ")
print("os.getcwd()=",os.getcwd())
os.chdir("..")
print("os.getcwd()=",os.getcwd())