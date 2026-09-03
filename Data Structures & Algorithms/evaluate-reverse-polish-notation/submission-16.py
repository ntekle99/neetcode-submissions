import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_stack = []
        numbers_stack = []

        for i in range(len(tokens)):
            if tokens[i] == '*' or tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '/':
                operation_stack.append(tokens[i])
            else:
                numbers_stack.append(tokens[i])
            if len(operation_stack) > 0:
                operation = operation_stack.pop()
                val_1 = numbers_stack.pop()
                val_2 = numbers_stack.pop()
                if operation == '*':
                    final_result = int(int(val_2) * int(val_1))
                if operation == '+':
                    final_result = int(int(val_2) + int(val_1))
                if operation == '/':
                    final_result = int(int(val_2) / int(val_1))
                if operation == '-':
                    final_result = int(int(val_2) - int(val_1))
                numbers_stack.append(final_result)
        return int(numbers_stack.pop())

            
        