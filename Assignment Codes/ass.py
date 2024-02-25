count=0
count2=0
s=(input("Enter Word In Capital Letter="))
l=len(s)
for i in range (0,l):
    if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O'or s[i]=='U'):
        count=count+1
    else:
        count2=count2+1
print(count)
print(count2)
print(l-count)