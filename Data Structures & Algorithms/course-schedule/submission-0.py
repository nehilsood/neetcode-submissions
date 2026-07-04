class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = collections.defaultdict(list)
        indeg = [0]*numCourses
        for c1,c2 in prerequisites:
            course_dict[c1].append(c2)
            indeg[c2] += 1

        q = collections.deque()
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in course_dict[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
        


        