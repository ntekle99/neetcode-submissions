class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stk.append(s[i])
            elif s[i] == ']' or s[i] == '}' or s[i] == ')':
                if len(stk) == 0:
                    return False
                element = stk.pop()
                if element == '[' and s[i] == ']':
                    continue
                elif element == '{' and s[i] == '}':
                    continue
                elif element == '(' and s[i] == ')':
                    continue
                else:
                    return False           
        
            else:
                return False
        return True if len(stk) == 0 else False