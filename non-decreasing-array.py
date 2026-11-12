class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        prev = 0
        violations_count = 0
        v_prev = 0
        v_curr = 0
        for curr in range(len(nums)):
            violations_count += nums[curr] < nums[prev]
            if nums[curr] < nums[prev]:
                v_prev = prev
                v_curr = curr
            prev = curr
        if violations_count != 1:
            return violations_count <= 1
        if v_prev == 0 or v_curr == len(nums) - 1:
            return True
        # need to check surroundings
        changes_needed = nums[v_curr] < nums[v_prev - 1]
        changes_needed += nums[v_curr + 1] < nums[v_prev]

        return changes_needed < 2
