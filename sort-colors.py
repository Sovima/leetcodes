class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        
        for i in nums:
            zeros += i == 0
            ones += i == 1
            twos += i == 2
        nums[0:zeros] = [0] * zeros
        nums[zeros:zeros+ones] = [1] * ones
        nums[ones+zeros:zeros+ones+twos] = [2]*twos
        return nums
       
