class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        longest = 0
        num_set = set(nums)
        for x in nums:
            num = x
            current = 1
            if (x - 1) not in num_set:
                while (num + 1) in num_set:
                    num += 1
                    current += 1
            if current >= longest:
                longest = current
        
        return longest
