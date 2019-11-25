def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        while 2**i<=num:
            i+=1
        return(2**i-num-1)