import math
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i=0
        curr_num = ""
        while i < len(s):
            if s[i] != "#":
                curr_num += str(s[i]) 
                i+=1
                continue
            else:
                i+=1
                lst.append(s[i:i+int(curr_num)])
                i = i+int(curr_num)
                curr_num = ""
        
        return lst
        
        
        
        
        
        
        # expected_cnt = 0
        # lst = []
        # curr_word = ""
        # i=0
        # size = len(s)
        # for j in range(100):
        #     print(i)
        #     if i >= size:
        #         break
        #     if s[i] == "#":
        #         temp_i=i
        #         i+=1
        #         if expected_cnt == 0:
        #             i+=1
        #         else:
        #             for j in range(math.ceil(expected_cnt/10)):
        #                 if s[i]!=str(expected_cnt)[0+j]:
        #                     i=temp_i
        #                     break
        #                 else:
        #                     i+=1
        #         if i == temp_i:
        #             curr_word = curr_word + "#"
        #         else:
        #             if curr_word != "":
        #                 lst.append(curr_word)
        #                 expected_cnt+=1
        #                 curr_word = ""
        #     else:
        #         curr_word = curr_word + s[i]
        #         i+=1
        # lst.append(curr_word)
        # return lst
                    

