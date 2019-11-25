  def isHappy(self,n):
        while True:
            if n<10:
                if n==1 or n ==7:
                    return True
                else:
                    return False
            n=sum([int(i)**2 for i in str(n)])