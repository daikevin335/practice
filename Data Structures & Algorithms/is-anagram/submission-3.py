class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial Check: if the strings are equal in length
        if (len(s) != len(t)):
            return False
        
        # create dicts for both s and t
        s_dict = {}
        t_dict = {}

        # record character counts for each s and t
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        # check if dicts are equal
        return s_dict == t_dict