class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words = sorted(words, key = lambda x: len(x))
        words = {i: 1 for i in words}
        for word in words.keys():
            for c in range(len(word)):
                try:
                    words[word] = max(words[word[:c] + word[c + 1:]] + 1, words[word])
                except:
                    continue
        return max(words.values())
        
