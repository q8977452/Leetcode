def addBinary(self, a, b):
        c=int(a,2)+int(b,2)
        x=bin(c).split('b')

        return x[1]
		#return bin(int(a,2)+int(b,2))[2:]