class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stk)!=0 and temperatures[i] > stk[-1][0]:
                lst = stk.pop()
                res[lst[1]] = i-lst[1]
                while True:
                    if len(stk) == 0:
                        break
                    if temperatures[i] > stk[-1][0]:
                        lst = stk.pop()
                        res[lst[1]] = i-lst[1]
                    else:
                        break
            
            stk.append([temperatures[i],i])
        return res