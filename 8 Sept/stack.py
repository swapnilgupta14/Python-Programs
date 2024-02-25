a=input()
n=len(a)
res=[-1]*n
st=[]
for i in range(n):
    while len(st)>0 and a[i]>a[st[-1]]:
        res[st[-1]]=a[i]
        st.pop()
    st.append(i)
print(res)