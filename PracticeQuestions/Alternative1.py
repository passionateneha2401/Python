def getAlternative(arr):
    for i in range(0,len(arr),2): #TC=O(n)             #range(0,4,2) TC=O(1)
        print (arr[i])
    
arr1 = [1,2,3,4]
arr2 = [1,2,3,4,5]

getAlternative(arr1)
getAlternative(arr2)



