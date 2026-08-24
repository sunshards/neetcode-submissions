class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t == "+":
                secondOperand = operands.pop()
                firstOperand = operands.pop()
                operands.append(firstOperand + secondOperand) 
            elif t == "-":
                secondOperand = operands.pop()
                firstOperand = operands.pop()
                operands.append(firstOperand - secondOperand) 
            elif t == "*":
                secondOperand = operands.pop()
                firstOperand = operands.pop()
                operands.append(firstOperand * secondOperand) 
            elif t == "/":
                secondOperand = operands.pop()
                firstOperand = operands.pop()
                operands.append( int(firstOperand /secondOperand) ) 
            else:
                operands.append(int(t))
        return operands.pop()