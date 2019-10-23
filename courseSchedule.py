from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # DFS
        def dfs(flags, curr, ad_map):
            if flags[curr] == 1: return False
            if flags[curr] == -1: return True
            flags[curr] = 1
            for n in ad_map[curr]:
                if not dfs(flags, n, ad_map): return False
            flags[curr] = -1
            return True
        
        flags = [0] * numCourses
        ad_map = defaultdict(list)
        for cur,pre in prerequisites:
            ad_map[pre].append(cur)
        for curr in range(numCourses):
            if not dfs(flags, curr, ad_map): return False
        return True
            
        # BFS
        """
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
        """
