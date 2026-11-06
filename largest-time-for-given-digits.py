class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:

        def time_valid(a, b, c, d):
            valid = True
            if a > 2 or c > 5:
                return False
            if a == 2 and b > 3:
                return False
            return valid

        max_time = [-1, 0, 0, 0]
        for i in permutations(arr):
            if time_valid(i[0], i[1], i[2], i[3]):
                new_time = [i[0], i[1], i[2], i[3]]
                bigger_time = int("".join([str(j) for j in i])) > int("".join([str(j) for j in max_time]))
                max_time = new_time if bigger_time else max_time
        time = f"{max_time[0]}{max_time[1]}:{max_time[2]}{max_time[3]}"
        return "" if max_time[0] == -1 else time


        
