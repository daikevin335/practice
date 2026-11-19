class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        highest = 0
        right = left
        count = 0
        seen = set()
        while (right >= left) and (right < len(s)):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
                count = right - left 
            else: 
                seen.add(s[right])
                count += 1
                highest = max(highest, count)
                right += 1 

        return highest



