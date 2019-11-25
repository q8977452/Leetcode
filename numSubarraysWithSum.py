class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
		reg=0
        for (i in range(len(A)):
            count = 0
            for (j in range(i, len(A)+1)):
                if (A[j] == 1):
					count += 1
				if (count == S):
					reg += 1
						if (A[j+1]) == 1:
							break
		
		return(reg)
				
				