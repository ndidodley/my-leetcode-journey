def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) != len(set(nums)):
        return True
    else:
        return False