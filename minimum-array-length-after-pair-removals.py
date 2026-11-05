class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        middle = len(nums) // 2
        odd = len(nums) % 2
        left = middle - (1 - odd)
        right = middle 
        while right < len(nums) and nums[right] == nums[middle]:
            right += 1
        right -= int(right >= len(nums) or nums[right] != nums[middle])
        while left >= 0 and nums[left] == nums[right]:
            left -= 1
        left += int(left < 0 or nums[left] != nums[right])
        if nums[right] != nums[left]:
            return odd
        common = right - left + 1
        return max(common - (len(nums) - common), odd)
        
