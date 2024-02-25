def TowerofHanoi(n,source,auxillary,destination):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    TowerofHanoi(n-1,source,destination,auxillary)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerofHanoi(n-1,auxillary,source,destination)

n=4
TowerofHanoi(n,'A','B','C')
