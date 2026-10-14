class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for wrd in strs:
            key = "".join(sorted(wrd))  
            if key in group:
                group[key].append(wrd)
            else:
                group[key] = [wrd]
        
        return list(group.values())



