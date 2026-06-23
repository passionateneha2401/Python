class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = [1,3]
        nums2 = [2]

        m = len(nums1)
        n = len(nums2)

        nums3 = nums1 + nums2

        length = len(nums3)

        for i in range(length):
            for j in range(i+1,length):
                if(nums3[i]>nums3[j]):
                    nums3[i], nums3[j] = nums3[j], nums3[i]

        if(length % 2 == 1):
            return float(nums3[length // 2])
        else:
            return float((nums3[len //2 -1] + (nums3[len // 2])) / 2.0)
        
        

     
s = Solution()
s.findMedianSortedArrays([1,3],[2])

s.findMedianSortedArrays([1,2],[3,4])





