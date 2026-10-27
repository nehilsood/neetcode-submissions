class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def get_freq(word):
            key = [0]*26
            for letter in word:
                key[ord(letter)-ord('a')] += 1
            
            return key
        
        ans = []
        window_size = len(p)
        key_p = get_freq(p)
        for i in range(len(s)-len(p)+1):
            temp = s[i:i+window_size]
            if get_freq(temp) == key_p:
                ans.append(i)

        return ans






