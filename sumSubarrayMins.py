def sumSubarrayMins(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
	temp_sum=0
	temp_sum +=sum(A)
    #return min(A[0:1])
    for j in range(len(A)):
		for i in range(j):
            temp_sum += min(A[i:len(A)+i+1-j])
    
    return temp_sum
            