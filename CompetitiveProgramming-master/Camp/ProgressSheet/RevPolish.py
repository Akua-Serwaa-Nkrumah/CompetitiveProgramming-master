import operator

class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
            
        stack = []
        ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/': operator.truediv}

        for i in range(len(tokens)):
            if tokens[i] in ops:
                curr = int(ops[tokens[i]](stack[-2],stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(curr)
                continue

            stack.append(int(tokens[i]))

        return curr
        