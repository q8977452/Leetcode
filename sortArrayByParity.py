def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    B=[]
    for i in range(len(A)):
        if A[i] % 2 ==0:
            B.append(A[i])
    for i in range(len(A)):
		if A[i] not in B:
			B.append(A[i])
    return B