class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # keep track of the total sum options in a matrix and then go through it
        # left to right to update whether this sum is possible or not
        # The main issue here is figuring out how to avoid duplicates 
        # (can't put the same item twice)

        # Maybe have a matrix len(nums) - 1 x sum(nums) // 2
        # The entry means whether a certain sum is possible up to the specified value
        # (the value can be included or not)
        if sum(nums) % 2: return False
        s_goal = sum(nums) // 2
        # make the matrix
        tracker = [i == 0 for i in range(s_goal + 1)]
        for i in range(len(nums)):
            # print(tracker)
            curr_tracker = [0 for i in range(s_goal + 1)]
            for s in range(s_goal + 1):
                curr_val = nums[i]
                # check if the specified sum can be generated 
                # with or without the current value
                curr_tracker[s] = tracker[s] or (s - curr_val >= 0 and tracker[s - curr_val])
            tracker = curr_tracker
        return tracker[s_goal]

