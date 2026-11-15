class Solution:
    def jump(self, nums: list[int]) -> int:
        # try finding the value with the furthest reach
        if len(nums) < 2:
            return 0
        
        max_reach = nums[0]
        start = 1
        end = min(max_reach, len(nums) -1)
        n_jumps = max_reach < (len(nums) - 1)
        while True:
            n_jumps += 1
            for i in range(start, end + 1):
                max_reach = max(max_reach, i + nums[i])
            start = end + 1
            end = min(max_reach, len(nums) - 1)
            
            if end == len(nums) - 1: return n_jumps
            
            
