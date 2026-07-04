class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for cur_x,cur_y in intervals[1:]:
            last = res[-1][1]
            if last >= cur_x:
                res[-1][1] = max(cur_y,last)
            else:
                res.append([cur_x,cur_y])
        
        return res

                
        