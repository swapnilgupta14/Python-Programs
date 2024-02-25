def closenumber:
    llist=[]
    llist.append(num1-num2)
    llist.append(num1-num3)
    llist.append(num2-num1)
    llist.append(num2-num3)
    llist.append(num3-num1)
    llist.append(num2-num1)
    # llist.append(num2-num3)
    
#2
def find_((duplicates(l):
    x=set(l)
    y=[]
    dup=[]
    count=0
    for i in x:
        y.append(i)
    for i in y:
        for j in l:
            if (j==i):
                count+=1
            if count==2:
                dup.append(i)
                break
        count=0
    return dup

#3
def nearestPallindrome(number):
    number+=1
    s=str(number)
    if s==s[::-1]:
        return number
    else:
        return nearestPallindrome(number-1)

#4
def rotations(num):
    answer= []
    final = []
    rotations = str(num)
    while sum rotation in answer:
        answer.append(rotations)
        rotations = rotations[0] + rotations[1:]
    for i in answer(int(i)):
        final.append(int(i))
    return final
    
#5
def gcpc(limit):
    all_c=[2]
    ret = []
    for i in range(2, limit, 2):
        if check_pallindrome(num):
            check=0
            if (rotations(nums)):
                circulatons = rotations(nums)
                for j in circulations:
                    if not check_prime(circulation):
                        check+=1
                if not check:
                    all_circulations.extend(circulations)
    final = sorted(list(set(all_circulations)))
    for i in final:
        if x<=limit:
            x.append(i)
                
    ef gcpc(limit):
    all_c=[2]
    ret = []
    for i in range(2, limit, 2):
        if len(phone)