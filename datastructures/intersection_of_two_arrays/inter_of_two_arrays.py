def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1s = set(nums1)
    nums2s = set(nums2)

    sols = list(nums1s.intersection(nums2s))
    resols = []
    for i in sols:
        count1 = nums1.count(i)
        count2 = nums2.count(i)

        if count1 <= count2:
            resols.extend([i] * count1)
        else:
            resols.extend([i] * count2)