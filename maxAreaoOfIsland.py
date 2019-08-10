class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        res = 0 
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    continue
                print(i,j)
                counter, q, grid[i][j] = 1, [(i,j)], 0 
                while q:
                    node = q.pop(-1)
                    x, y = node
                    grid[x][y] = 0
                    if x-1 >= 0 and grid[x-1][y] == 1:
                        q.append((x-1,y))
                        grid[x-1][y] = 0
                        counter += 1
                    if x+1 < m and grid[x+1][y] == 1:
                        q.append((x+1,y))
                        grid[x+1][y] = 0
                        counter += 1
                    if y-1 >= 0 and grid[x][y-1] == 1:
                        q.append((x,y-1))
                        grid[x][y-1] = 0
                        counter += 1
                    if y+1 < n and grid[x][y+1] == 1:
                        #print("hot in")
                        q.append((x,y+1))
                        grid[x][y+1] = 0
                        counter += 1
                res = max(res, counter)
        return res
