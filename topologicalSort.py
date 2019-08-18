class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #return self.top_sort(numCourses, prerequisites)
	#hihi
        return self.top_sort(numCourses, prerequisites)
    
    def top_sort(self, numCourses, prerequisites):
        from collections import defaultdict
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0]) 
            in_degree[p[0]] += 1
        q = list()
        count = 0
        for c in range(numCourses):
            if in_degree[c] == 0:
                q.append(c)
                count += 1
        while q:
            c = q.pop()
            for cc in graph[c]:
                in_degree[cc] -= 1
                if in_degree[cc] == 0:
                    q.append(cc)
                    count += 1
        return count == numCourses
