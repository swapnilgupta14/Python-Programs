from pickle import TUPLE1

arr=['Swapnil','The','Great']
print(enumerate(arr))
print(list(enumerate(arr)))
print(tuple(enumerate(arr)))
# eumerate assign the respective value/index to the respective value of iteration 
print("\n")
for i, j in enumerate(arr):
     print(i,"===",j)
print("\n")
#
for a in enumerate(arr):
     print("a=",a,"\t",type(a))
print('\n')
#
for i, j in enumerate(arr):
     print(i,"=",type(i))
     print(j,"=",type(j))