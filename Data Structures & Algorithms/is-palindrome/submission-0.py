class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():       
                cleaned += ch.lower()      
        left=0
        right=len(cleaned)-1
        for i in range(len(cleaned)//2):
            if cleaned[left]==cleaned[right]:
                left=left+1
                right=right-1
            else:
                return False
        return True