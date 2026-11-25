class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def product_eq(vals):
            ones = vals[1]
            total = sum([vals[i] for i in vals])
            rest = total - ones
            if total <= 2:
                return True
            repeat = sum([1 for i in vals if vals[i] > 1 and i != 1])
            twos = sum([1 for i in vals if i % 2 == 0 and vals[i] > 0])
            threes = sum([1 for i in vals if i % 3 == 0 and vals[i] > 0])
            fives = sum([1 for i in vals if i % 5 == 0 and vals[i] > 0])

            return repeat == 0 and twos <= 1 and threes <= 1 and fives <= 1
        

        start = 0
        end = 1
        max_len = 1
        if len(nums) <= 2: return(len(nums))
        from collections import defaultdict
        vals = defaultdict(int)
        vals[nums[start]] += 1
        vals[nums[end]] += 1
        while end < len(nums) and start <= end:
            if product_eq(vals): 
                max_len = max(end - start + 1, max_len)
                end += 1
                if end < len(nums):
                    vals[nums[end]] += 1
            else: 
                vals[nums[start]] -= 1
                start += 1
                continue
            
        return max_len
        
