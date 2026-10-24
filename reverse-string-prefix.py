class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        j = k - 1
        temp = ""
        for j in range(k - 1, -1, -1):
            temp += s[j]
        return temp + s[k:]
