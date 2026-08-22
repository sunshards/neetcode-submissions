class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<j:
            while not self.alphaNumeric(s[i]) and i < j:
                i+=1
            while not self.alphaNumeric(s[j]) and j > i:
                j-=1

            if (s[i].lower() != s[j].lower()):
                return False
            i+=1
            j-=1

        return True
    
    # Or s.isalnum() default in python
    def alphaNumeric(self, c):
        return  (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9"))
