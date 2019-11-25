def findMaxConsecutiveOnes(self, nums):
        temp_high,end_high=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                temp_high+=1
                if temp_high >end_high:
                    end_high=temp_high
            else:
                temp_high=0
        return end_high