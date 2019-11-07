from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        m = defaultdict(list)
        queue = [i for i in range(numCourses)]
        seen = set(queue)
        for course, preq in prerequisites:
            if course in seen:
                queue.remove(course)
                seen.remove(course)
            m[course].append(preq)
        flag = True
        while flag:
            flag = False
            for c, preqs in m.items():
                tmp = preqs[:]
                for p in preqs:
                    if p in seen:
                        tmp.remove(p)
                m[c] = tmp
                if len(m[c]) == 0:
                    queue.append(c)
                    seen.add(c)
                    del m[c]
                    flag = True
        if len(queue) == numCourses:
            return queue
        return []

        """ 
        in_degree = {i:0 for i in range(numCourses)}
        graph = {i:set() for i in range(numCourses)}
        for c,p in prerequisites:
            graph[p].add(c)
            in_degree[c] += 1
        stack, res = [], []
        for c, d in in_degree.items():
            if d == 0:
                stack.append(c)
        while stack:
            node = stack.pop(-1)
            res.append(node)
            for i in graph[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    stack.append(i)
        return [] if len(res) != numCourses else res
        """
