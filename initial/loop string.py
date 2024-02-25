arr=[] #empty  array
print("Arrray Before=",arr)
count=0
while(True):
    s1=input("Enter any friend name: ")
    if(len(s1)>4):
        arr.append(s1)
    elif(len(s1)<=4):
        count=count+1
    choice=input("Wish to add more?(y/n) :")
    if(choice=='n'):
        break
print("Friends names less than 4=",count)
print("Array-After=",arr)