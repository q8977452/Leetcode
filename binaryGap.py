def binaryGap(self,N):
    curPos,lastOnePos,maxDis=0,-1,0
    while N:
		if N%2 == 1:
			if lastOnePos != -1:
				maxDis = max(curPos - lastOnePos, maxDis)
            lastOnePos = curPos
		N /= 2
        N=int(N)    
        curPos+=1            
	return maxDis
         