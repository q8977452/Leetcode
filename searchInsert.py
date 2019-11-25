def searchInsert(self, nums, target):
        count=0
        for i in range(len(nums)):
            if target<=nums[i]:
                return count
            elif target>nums[i]:
                count+=1
        return count