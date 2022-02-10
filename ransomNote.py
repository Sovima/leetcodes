class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = dict()
        for c in magazine:
            if c in seen:
                seen[c] = seen[c] + 1
            else:
                seen[c] = 1
        for i in ransomNote:
            check = seen.get(i)
            if check:
                seen[i] = check - 1
            else:
                return False
        return True 
