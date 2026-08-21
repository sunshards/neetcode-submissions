class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s))
            output += "/" # to interrupt counting
            output += s
        return output

    def decode(self, s: str) -> List[str]:
        output=[]
        i=0
        ls=""
        while i<len(s):
            while s[i] in "0123456789":
                ls+=s[i]
                i+=1
            l = int(ls)
            # Begin from i+1 to avoid /
            output.append(s[i+1:i+l+1])
            i+=l+1
            ls=""

        return output