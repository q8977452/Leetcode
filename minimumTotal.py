def minimumTotal(self, triangle):
	
	n=len(triangle)
    for i in range(n):
        for j in range(0,i+1):
            if i== 0:
				triangle[i][j] = triangle[i][j]
            elif j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j]+min(triangle[i-1][j-1], triangle[i-1][j])
                    
	return min(triangle[n-1]) 