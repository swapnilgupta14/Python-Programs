#include<stdio.h>
int main()
{   
    int res=0,key
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    scanf("%d",&key);
    res=search(arr[],key);
    print("%d",res);
}
int search(int arr[],int n,int key)
{
    for(int i=0;i<n;i++)
        if(arr[i]==key)
            return i;
}