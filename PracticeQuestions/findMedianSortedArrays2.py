def findMedianSortedArrays(nums1,nums2):
    nums3 = nums1 + nums2
    length = len(nums3)

    for i in range(length):
        for j in range(i+1,length):
            if(nums3[i]>nums3[j]):
                nums3[i],nums3[j] = nums3[j],nums3[i]

    print(nums3)

    if(length % 2 == 1):
        return float(nums3[length // 2])
    else:
        return (nums3[length//2-1]+nums3[length//2])/2.0
    


def main():
    print(findMedianSortedArrays([1,3],[2]))
    print(findMedianSortedArrays([1,2],[3,4]))


if __name__ == "__main__":
    main()