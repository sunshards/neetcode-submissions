
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combos = {}
        output = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
    
            key = tuple(count)
            if key not in combos:
                combos[key] = [s]
            else:
                combos[key].append(s)
        for k in combos:
            output.append(combos[k])
        return output

