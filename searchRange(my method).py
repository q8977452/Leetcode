def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x=[]
        for i in range(len(nums)):
            if nums[i] == target:
                x.append(i)
        if len(x)>1:
            return [x[0],x[-1]]
        elif len(x) == 1:
            return [x[0],x[0]]
        else:
            return [-1,-1]