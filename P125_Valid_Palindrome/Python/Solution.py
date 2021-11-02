class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [t.lower() for t in s if t.isalnum()]
        start = 0
        end = len(a)-1
        while start<end:
            if(a[start] != a[end]):
                return False
            start +=1
            end -=1
        return True