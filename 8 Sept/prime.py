flag=0
n=int(input("Enter The number:"))
for i in range(2,n//2):
#modulus-remainder, floor division se int part, single / se float ans 
    if(n%i==0):
        flag=flag+1
if(flag!=0):
    print("Not A prime")                                                                  #--- Normal zindagi
else:
    print("Prime")

num=int(input("Enter number for prime number testing :"))
r=[n for n in range(2,num) if num%n==0] 
#ismee for ke andar hai if ki condition aur if ke andar hai n jokii fill ho rha hai array me --- Mentos zindagi
if(len(r)<0):
    print("prime")
else:
    print("Not prime")
