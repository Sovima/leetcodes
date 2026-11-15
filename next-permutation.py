class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        if len(nums) == 2:
            f = nums[0]
            nums[0] = nums[1]
            nums[1] = f
            return 
        flipped=False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                # Found the first drop, flip the middle 
                temp = nums[i - 1] # This value will be added to the first section
                # Find next larger value in the first half compared to the middle
                s = i
                while s < len(nums) and nums[i - 1] < nums[s]:
                    s += 1
                s = max(i, min(s - 1, len(nums) - 1))
                nums[i - 1] = nums[s]
                nums[s] = temp
                flipped=True
                break
        # Flip all nums between i and the end of the list

        if i == 1 and not flipped:
            i = 0
        for j in range((len(nums) - i) // 2):
            temp = nums[i + j]
            nums[i + j] = nums[len(nums) - 1 - j]
            nums[len(nums) - 1 - j] = temp
        return nums
