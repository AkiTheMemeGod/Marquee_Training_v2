class Solution(object):
    def uniquepaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        hashmap = {}
        for i in range(0, m):
            hashmap[(i, 0)] = 1
        for j in range(0, n):
            hashmap[(0, j)] = 1

        for i in range(1, m):
            for j in range(1, n):
                hashmap[(i,j)] = hashmap[(i - 1, j)] + hashmap[(i, j - 1)]

        return hashmap[(m-1,n-1)]

s = Solution()
x = s.uniquepaths(3, 3)
print(x)    