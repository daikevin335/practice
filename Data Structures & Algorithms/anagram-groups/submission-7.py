class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sort each word in alphabetical order
        # then store original word of each sorted repeat in dict

        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        # only care about the values of each key(sorted word)
        return list(groups.values())
            



