class Solution:

    def encode(self, strs: List[str]) -> str:
        final_s = ""
        for s in strs:
            final_s = final_s + str(len(s)) + "#" + s
        return final_s


    def decode(self, s: str) -> List[str]:
        print(s)
        cnt = 0
        rd_cnt = 0
        lst = []
        while True:
            print(cnt)
            if cnt == len(s):
                break
            if s[cnt] !="#":
                rd_cnt = (rd_cnt*10)+int(s[cnt])
            elif s[cnt]=="#":
                lst.append(s[cnt+1:rd_cnt+cnt+1])
                cnt+=rd_cnt
                rd_cnt = 0
            cnt+=1
        return lst


