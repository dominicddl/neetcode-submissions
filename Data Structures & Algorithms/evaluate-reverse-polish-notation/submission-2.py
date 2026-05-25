class Solution:
    def isInteger(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError: 
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        res = 0
        for i in range(len(tokens)):
            if self.isInteger(tokens[i]):
                stack.append(tokens[i])
            if tokens[i] in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i] == "+":
                    res = int(op1) + int(op2)
                elif tokens[i] == "-":
                    res = int(op1) - int(op2)
                elif tokens[i] == "*":
                    res = int(op1) * int(op2)
                elif tokens[i] == "/":
                    res = int(op1) / int(op2)
                stack.append(res)
        return int(stack.pop())