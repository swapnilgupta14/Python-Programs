from itertools import permutations
list1=['a','b']
list2=[1,2]
for per in sorted(list(permutations(list1,len(list2)))):
    print(''.join(per))
for i in sorted(list(permutations(list2,len(list1)))):
    print(''.join(i))