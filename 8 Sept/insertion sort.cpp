#include <math.h>
#include <stdio.h>
void insertionSort(int A[], int n)
{
	int i,key,j;
	for (i=1;i<n;i++)
	{
		key=A[i];
		j=i-1;
		while(j>=0 && A[j]>key)
		{
			A[j+1]=A[j];
			j=j-1;
		}
		A[j+1]=key;
	}
}

















void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		printf("%d ", arr[i]);
	printf("\n");
}
int main()
{
	int arr[]={12, 11, 13, 5, 6};
	int n = sizeof(arr) / sizeof(arr[0]);
	insertionSort(arr, n);
	printArray(arr, n);
	return 0;
}
