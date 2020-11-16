def arrayPairSum(self, nums):
        pair_sum=0
        if len(nums)%2!=0:
            return False
        nums.sort()
        for i in range(1,len(nums)+1,2):
            pair_sum+=min(nums[i],nums[i-1])
        return pair_sum
        #return sum([nums[i] for i in range(0,len(nums),2)])