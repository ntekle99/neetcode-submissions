class Solution:
    def isValid(self, s: str) -> bool:
        lst =[]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i]=='[':
                lst.append(s[i])
            else:
                if lst == []:
                    return False
                temp = lst.pop()
                if s[i] == '}' and temp!='{':
                    return False
                if s[i] == ']' and temp!='[':
                    return False
                if s[i] == ')' and temp!='(':
                    return False
        return len(lst) == 0
                    
        