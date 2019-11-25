def canMeasureWater(self, x, y, z):
        from fractions import gcd
		if z==0 or x+y>=z and z % gcd(x, y) == 0:
            return True
        return False
        return z == 0 or x + y >= z and z % gcd(x, y) == 0
