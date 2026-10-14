class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial Check: if the strings are equal in length
        if len(s) != len(t):
            return False

        # Create dictionary for both s and t
        s_dict = {}
        t_dict = {}

        # fill char values in s dict, count how many of each char 
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        # fill char values in t dict, count how many of each char 
        for char in t:
            if char in t_dict:
                t_dict[char] +=1 
            else:
                t_dict[char] = 1
        

        # compare if dicts are equal
        return s_dict == t_dict
        