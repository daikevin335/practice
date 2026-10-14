class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            # Check to see if diff between target and current number in dict is in seen array
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            # if not, add current number to dict array 
            else:
                seen[num] = i