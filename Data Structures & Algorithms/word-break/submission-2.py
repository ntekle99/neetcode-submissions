class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)

        memo = {}
        def dfs(curr_s):
            if curr_s in memo:
                return memo[curr_s]
            if len(curr_s) == 0:
                return True
                
            curr_word = ""
            print(curr_s)
            res = False

            for i in range(len(curr_s)):
                curr_word = curr_word + curr_s[i]
                if curr_word in st:
                    res = dfs(curr_s[i+1:])
                    memo[curr_s[i+1:]] = res
                if res:
                    return res

            return False
        return dfs(s)
            


        