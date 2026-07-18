nums1 = [1,3]
nums2 = [2]

nums3 = nums1 + nums2

length = len(nums3)

for i in range(length):
    for j in range(i+1,length):
        if(nums3[i]>nums3[j]):
            nums3[i], nums3[j] = nums3[j],nums3[i]

print(nums3)

if(nums3 % 2 == 1):
    return float()
