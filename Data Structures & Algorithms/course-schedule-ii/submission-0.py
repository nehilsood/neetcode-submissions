class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dict = collections.defaultdict(list)
        indeg = [0]*numCourses
        for c1,c2 in prerequisites:
            course_dict[c1].append(c2)
            indeg[c2] += 1

        q = collections.deque()
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)

        finish,res = 0,[]
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for nei in course_dict[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        return res[::-1]

        