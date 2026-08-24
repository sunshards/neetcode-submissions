class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesisMap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in parenthesisMap:  # c is a closing bracket
                if not stack or stack.pop() != parenthesisMap[c]:
                    return False
            else:  # c is an opening bracket
                stack.append(c)

        return len(stack) == 0