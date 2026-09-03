class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=list(s)
        arr_2=list(t)
        arr.sort()
        arr_2.sort()
        return arr == arr_2