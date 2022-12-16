class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(item for item in s if item.isalnum())
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                 return False
            l+=1
            r-=1     
        return True
                 
            
