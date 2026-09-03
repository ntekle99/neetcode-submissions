class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n in memo:
        #     return memo[n]
        # memo[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        # return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        for i in range(2,len(arr)):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]
        
        