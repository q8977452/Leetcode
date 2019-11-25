def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        count=0
        for i in range(1,n+1):
            x=math.log(i,5)
            if x.is_integer() :
                count+=int(math.log(i,5))
            else:
                while i%5 ==0:
                    count+=1
                    i/=5
        return count