#for kii coding for ke phle hoti hai aur for kii condition for ke baad hoti hai
arr=[1,2,3,4,5,6,7,8,9,10]

b=[m*10 for m in arr if m%3!=0]
# or this can be written as -
# b=[]
# for m in arr:
#     if(m%3!=0):
#         b.append(m*10)
print(b)