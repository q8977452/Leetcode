def uncommonFromSentences(self, A, B):
        A_split=A.split()
        B_split=B.split()
        C_split=A_split+B_split
        i = 0
        while i < len(C_split):
            val = C_split[i]
            count = C_split[0:len(C_split)].count(val)
            
            if 1< count:
                j=0
                while j <count:
                    
                    del C_split[C_split.index(val)]
                
                    j += 1
                i = i
            else:
                i +=1
        return C_split
    