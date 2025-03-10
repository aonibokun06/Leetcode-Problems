# Easy
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        for right in range(1,len(nums)):
            if nums[right]!=nums[left]:
                left+=1
                nums[left]=nums[right] 
        return left+1