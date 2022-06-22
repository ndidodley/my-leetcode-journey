def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    count = 0
    # start from the end (num1) and replace each item with items from nums2
    for i in range(len(nums1) - 1, -1, -1):
        # loop till the end of the array num2
        if count == n:
            break
        nums1[i] = nums2[count]
        count += 1
    nums1.sort()
    print(nums1)


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # inefficient
    nums1[m:] = nums1
    nums1.sort()
