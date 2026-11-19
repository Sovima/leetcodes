class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3: return 0
        small = []
        big = []
        for i in nums:
            small.append(i)
            big.append(i)
            small = sorted(small)[0:3]
            big = sorted(big, reverse = True)[0:3]
        # evaluate the 3 possible options
        # both bring in
        o1 = big[1] - small[1]
        # small bring in
        o2 = big[0] - small[2]
        # big bring in
        o3 = big[2] - small[0]
        return min([o1, o2, o3])
        
        
        
