class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == "":return s
        max_len = 1
        palindrome = s[0]
        for c in range(len(s) * 2):
            center = 0.5 * c
            start = math.floor(center)
            end = math.ceil(center)
            equal = int(start == end)
            start -= equal
            end += equal
            while start >=0 and end<len(s):
                if s[start] == s[end]:
                    if end - start + 1 > max_len:
                        palindrome = s[start:end + 1]
                        max_len = end - start + 1
                    start -= 1
                    end += 1
                else: 
                    break
        return palindrome
        
