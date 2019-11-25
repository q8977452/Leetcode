class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A.sort();B.sort();C.sort();D.sort()
        temp,res,target=0,set(),{}
        lena,lenb,lenc,lend=len(A),len(B),len(C),len(D)
        if lena==0 or lenb==0 or lenc==0 or lend ==0:
            return temp
        for p in range(lena):
            for q in range(lenb):
                if A[p]+B[q] not in target:
                    target[A[p]+B[q]]=[(p,q)]
                else:
                    target[A[p]+B[q]].append((p,q))
        for i in range(lenc):
            for j in range(lend):
                T=0-C[i]-D[j]
                if T in target:
                    for k in target[T]:
                        temp+=1
        return temp