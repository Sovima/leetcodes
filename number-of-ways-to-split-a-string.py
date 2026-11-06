class Solution:
    def numWays(self, s: str) -> int:
        ones = sum([1 for i in s if i == "1"])
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return ((len(s) - 2) * (len(s) - 1) // 2) % 1000000007
        
        third_ones = ones // 3
        start1 = 0
        while third_ones > 0:
            third_ones -= int(s[start1] == "1")
            start1 += 1
        end1 = start1
        while s[end1] != "1":
            end1 += 1
        start2 = end1
        third_ones = ones // 3
        while third_ones > 0:
            third_ones -= int(s[start2] == "1")
            start2 += 1
        end2 = start2
        while s[end2] != "1":
            end2 += 1
        
        return (end1 - start1 + 1) * (end2 - start2 + 1) % 1000000007
