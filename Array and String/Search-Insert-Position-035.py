# Easy
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity

def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # Binary Search
        while left <= right:   
            middle = (left+right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return left