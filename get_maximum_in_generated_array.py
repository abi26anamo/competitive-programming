class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for i in range(n+1)]
        if n==0:
            return 0
        if n==1:
            return 1
        nums[0] =0
        nums[1]=1
        for i in range(2,n+1):
            if i%2==0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2]+nums[i//2+1]
        return max(nums)
