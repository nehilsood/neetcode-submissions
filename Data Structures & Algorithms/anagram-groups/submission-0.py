from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq_array(word):
            arr = [0]*26
            for s in word:
                arr[(ord(s) - ord("a"))] += 1

            return arr

        hashmap = defaultdict(list)
        for word in strs:
            freq_arr = get_freq_array(word)
            hashmap[tuple(freq_arr)].append(word)
        
        res = []
        for key in hashmap:
            res.append(hashmap[key])
        
        return res
        
        