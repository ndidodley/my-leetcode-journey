def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum2(self, nums: List[int], target: int) -> List[int]:
    idx = {}
    for index, value in enumerate(nums):
        rem = target - value
        if value in idx:
            return [idx[value], index]

        idx[rem] = index

