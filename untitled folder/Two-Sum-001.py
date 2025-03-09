def twoSum(self, nums: List[int], target: int) -> List[int]:
    table = {}
    n = len(nums)
    for i, num in enumerate(nums):
        diff = target - num
        if diff in table:
            return [i, table[diff]]
        table[num] = i
    return []