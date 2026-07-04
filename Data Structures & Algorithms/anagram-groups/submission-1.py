from collections import defaultdict
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        def create_key(word):
            key = [0]*26
            for letter in word:
                index = ord(letter) - ord("a")
                key[index] += 1
            return tuple(key)

        _dict = defaultdict(list)
        for word in words:
            key = create_key(word)
            _dict[key].append(word)

        result = []
        for key in _dict:
            result.append(_dict[key])
        
        return result


        