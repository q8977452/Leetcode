def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1
		#return int((len(nums)+1)*len(nums)/2-sum(nums))