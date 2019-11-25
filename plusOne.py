def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        t = 1
        for i in digits[::-1]:
            i = i + t 
            if i >= 10:
                res.append(i-10)
                t = 1
            else:
                res.append(i)
                t = 0
        if t == 1:
            res.append(t)
        return res[::-1]