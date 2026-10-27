class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        start = 0        
        fast = start
        slow = start
        l = len(nums)
        while True:
            slow = (slow + nums[slow]) % l
            fast = (fast + nums[fast]) % l
            fast = (fast + nums[fast]) % l
            if slow == fast:
                # cycle found
                if (nums[slow] % l != 0):
                    positive = True
                    negative = True
                    while nums[slow] != 0:
                        positive = positive and nums[slow] >= 0
                        negative = negative and nums[slow] <= 0
                        t = (slow + nums[slow]) % l
                        nums[slow] = 0
                        slow = t
                    if positive or negative:
                        return True
                else:
                    slow = start
                    while nums[slow] != 0:
                        t = (slow + nums[slow]) % l
                        nums[slow] = 0
                        slow = t
                # Find next start
                while start < l and nums[start] == 0:
                    start += 1
                if start == l:
                    return False
                slow = start
                fast = start
        return False


        
