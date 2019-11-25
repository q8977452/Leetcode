class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        x=int(c**(1/2))
        if x**2==c:
            return True
        for a in range(x+1):
            for b in range(x+1):
                if a**2+b**2==c:
                    return True
        return False