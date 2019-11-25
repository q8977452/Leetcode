def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        count=0
        import math as m
        for i in range(1,n+1):
            x=math.log(i,10)
            while i>0:
                if i%10 == 1:
                    count+=1
                    i=(i-i%10)/10
                else:
                    i=(i-i%10)/10
        return count