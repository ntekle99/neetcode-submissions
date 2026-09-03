class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for val in tokens:
            if val!= "+" and val!="-" and val!="*" and val!="/":
                stk.append(val)
            else:
                element_1 = stk.pop()
                element_2 = stk.pop()
                if val == "+":
                    stk.append(int(element_1)+int(element_2))
                if val == "*":
                    stk.append(int(element_1)*int(element_2))
                if val == "-":
                    stk.append(int(int(element_2)-int(element_1)))
                if val == "/":
                    stk.append(int(element_2)/int(element_1))
            print(stk)

        return int(stk[-1])