class Solution(object):
    def util(self, m, n, hashmap):
        print(hashmap)
        if m == 1 or n == 1:
            return 1
        if hashmap[(m, n)] != -1:
            return hashmap[(m, n)]
        if hashmap[(m, n)] != -2 or hashmap[(m, n)] != -1:
            hashmap[(m, n)] = self.util(m - 1, n, hashmap) + self.util(m, n - 1, hashmap)
        return hashmap[(m, n)]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid)
        hashmap = {}
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                hashmap[(i, j)] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    hashmap[(i, j)] = -2
        print(hashmap)
        result = self.util(m, n, hashmap)
        return result

s = Solution()
x = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(x)