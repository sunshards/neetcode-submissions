class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for x in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                old_temp, old_index = stack.pop()
                res[old_index] = i - old_index
            stack.append( (temperatures[i], i))
        return res