class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr_target = nums[i]
            l = i+1
            r=len(nums)-1
            while l < r:
                if nums[l]+nums[r]==-curr_target:
                    lst.append([curr_target,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l]+nums[r] < -curr_target:
                    l+=1
                else:
                    r-=1
        return lst
                
                

                    