def isUgly(self, num):
        if num <= 0 or num >= 2147483647:
            return False
        else:
            while num%2 ==0:
                num/=2
            while num%3 ==0:
                num/=3
            while num%5 ==0:
                num/=5
            if num ==1:
                return True
            else:
                return False 