class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = 1


        st = set()
        for num in dct:
            if num in st:
                continue

            curr_num = num+1
            while curr_num in dct:
                st.add(curr_num)
                dct[curr_num] = dct[curr_num-1] + 1
                curr_num+=1


        highest_seq = 0
        for num in dct:
            highest_seq = max(highest_seq,dct[num])
        
        return highest_seq