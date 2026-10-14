class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dict to keep track of nums and array spot 
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num 
            # is diff in dict? 
            if diff in seen: 
                return [seen[diff], i]
            else: 
                # if not add to dict w/ array spot 
                seen[num] = i
