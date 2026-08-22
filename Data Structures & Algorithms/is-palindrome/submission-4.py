class Solution:
    def isPalindrome(self, s: str) -> bool:

        i=0
        while i < len(s) and not s[i].isalnum() :
            print(i)
            i+=1
        j=len(s)-1
        while j>0 and not s[j].isalnum():
            j-=1

        while i<j:
            print(s[i].lower(), s[j].lower())
            if (s[i].lower() != s[j].lower()):
                return False
            i+=1
            while not s[i].isalnum() and i < len(s):
                i+=1
            j-=1
            while not s[j].isalnum() and j > 0:
                j-=1
        return True
