def transpose(self, A):
		if not A:
        return []
    m = len(A)
    n = len(A[0])
    
    res = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            res[i][j] = A[j][i]
    
    return res
        #return map(list,zip(*A))