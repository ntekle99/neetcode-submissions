class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        st = set()
        for i in range(len(nums)):
            curr_target = nums[i]
            l = i+1
            r=len(nums)-1
            while l < r:
                if nums[l]+nums[r]==-curr_target  and (curr_target,nums[l],nums[r]) not in st:
                    lst.append([curr_target,nums[l],nums[r]])
                    st.add((curr_target,nums[l],nums[r]))
                    l=i+2
                    r=len(nums)-2
                elif nums[l]+nums[r] < -curr_target:
                    l+=1
                else:
                    r-=1
        return lst
                
                

                    