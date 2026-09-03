class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct={}
        for val in strs:
            sorted_char = ''.join(sorted(val))
            if sorted_char in dct:
                dct[sorted_char].append(val)
            else:
                dct[sorted_char] = [val]
        return list(dct.values())