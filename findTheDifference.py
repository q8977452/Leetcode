def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res=ord(t[-1])
        for i in range(len(s)):
            res = res + ord(t[i]) - ord(s[i])
        return chr(res)