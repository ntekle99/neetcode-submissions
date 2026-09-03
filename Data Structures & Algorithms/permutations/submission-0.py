class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)

        def dfs(path):
            # base case: full permutation built
            if len(path) == len(nums):
                self.res.append(path.copy())
                return

            for i in range(len(nums)):
                if self.used[i]:
                    continue

                # pick
                self.used[i] = True
                path.append(nums[i])

                dfs(path)

                # unpick
                path.pop()
                self.used[i] = False

        dfs([])
        return self.res