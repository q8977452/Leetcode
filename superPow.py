#https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C++Java1-line-Python
def superPow(self, a, b):
        x=0
        for i in  range(len(b)):
            x+=b[i]*10**(len(b)-1-i)
        return a**x%1337
		#from functools import reduce
        #return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)