class Solution:
    def waveSort(self,arr):
        for i in range(0,len(arr)-1,2):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
       
    

object = Solution()
arr1 = [1,2,3,4,5]
object.waveSort(arr1)
for i in range(len(arr1)):
            print(arr1[i],end=" ")
    

'''
class Solution:
    def waveSort(self, arr):
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

obj = Solution()

arr1 = [1, 2, 3, 4, 5]

obj.waveSort(arr1)

for num in arr1:
    print(num, end=" ")
'''  
