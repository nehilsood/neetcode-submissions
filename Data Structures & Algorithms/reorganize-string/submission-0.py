from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = dict(Counter(s).most_common())
        pq = [(-freq,char) for char, freq in counter.items()]
        heapq.heapify(pq)
        if pq and -pq[0][0] > (len(s)+1)//2:
            return ""
        res = []
        prev_count,prev_char = 0,""

        while pq:
            count,char = heapq.heappop(pq)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(pq,(prev_count,prev_char))
            
            prev_count = count + 1
            prev_char = char

        return "".join(res)
