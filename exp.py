import itertools
# from itertools import permutations
 
# def cartesian_product(arr1, arr2):
#     return list(product(arr1, arr2))
   
# if __name__ == "__main__":
#     arr1 = ["a","b"]
#     arr2 = [1,2]
#     print(cartesian_product(arr1, arr2))

# from itertools import product
# list1=['a','b']
# list2=[1,2]
# u_c=[]
# u_c=list(list(zip(list1,element))for element in product (list2, repeat=len(list1)))
# print(u_c) 


# filter the list of student whose index is given in 
# test_list1=['kgf','is','not','best','and','not','cs']
# test_list2=['its ok','all ok','wrong','looks ok','wrong','ok','thats ok',]
# substr='ok'
# string=''
# for i in range(len(test_list2)):
#     if substr in test_list2[i]:
#         string+=test_list1[i]+" "
# print("\n")
# print(string)


#reverse k-slice the elements
# from itertools import islice
# test_list=[2,4,5,6,32,42,56,67,43,54,7,9,8]
# k=5
# empty=[]
# for i in range(len(test_list)-1,k+2,-1):
#     empty.append(test_list[i])
#     res=test_list[-k:][::-1]
#     res2=list(islice(reversed(test_list),k))
# print(empty)
# print(str(res))
# print(res2)


#make a python program to sort the list according accordig to the col using lambda
# arey=[[]]        
# def sortarray(array):
#     for i in range(len(array[0])):
#         sortedcolumn=sorted(array,key=lambda x.x[i])
#         print("sorted array specific to column {},{}".format(i,sortedcolumn))
# if __name__=='__main_':
#     array=[['java',1995],['c++',1953],['python',1989]]
#     sortarray(array)    
    
if __name__=='main':
    input[[1,2,3,4,5,6],[5,1,3,4],[9,5,7,1],[2,4,1,3]]
    print(combineall(input)) 
def combineall(input):
    result=set(input[0])
    for array in input[]:
        result.update(array)
    result_list(result)       