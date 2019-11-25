class Solution:
    def judgeSquareSum(self, c):
        x=int(c**(1/2))
        c=int(c)
        x+=1
        for i in range(2,x):
            count=0
            if c%i==0:
                while c%i==0:
                    count+=1
                    c /=i
                if i%4==3 and count %2 !=0:
                    return False
        return c % 4 !=3