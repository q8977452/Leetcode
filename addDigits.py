def addDigits(self, num):
        x=num
        while x >9:
            x=x%10+int(x/10)
        return x
		#return num if num == 0 else num % 9 or 9
