#to transform existing array into a new array by a shortcut method----List comprehension
arr=[i for i in range (1,11)]
#we are filling the empty array by a inside loop
print(arr)
#
arr=[i*i for i in range (1,11)]
print(arr)
#
arr=[i**.5 for i in range (1,11)]
print(arr)