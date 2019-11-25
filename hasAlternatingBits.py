def hasAlternatingBits(self, n):        
    cur,last=n%2,n%2
    n=int(n/2)
    while n >=1:
        last=cur
        if n%2 ==1:
			cur=1
        else:
            cur=0
        if  cur == last:
            return False
        n =int(n/2)
	return True
            