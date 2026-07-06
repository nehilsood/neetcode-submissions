class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_key(word):
            key = [0] * 32
            for letter in word:
                key[ord(letter) - ord("a")] += 1
            return key

        return get_key(s) == get_key(t)
        