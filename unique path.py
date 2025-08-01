class Solution(object):

    def util(self, m, n, hashmap):
        if m == 1 or n == 1:
            return 1
        if hashmap[(m, n)] != -1:
            return hashmap[(m, n)]
        hashmap[(m, n)] = self.util(m - 1, n, hashmap) + self.util(m, n - 1, hashmap)
        return hashmap[(m, n)]

    def uniquepaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        hashmap = {}
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                hashmap[(i, j)] = -1
        print(hashmap)

        result = self.util(m, n, hashmap)
        return result

s = Solution()
x = s.uniquepaths(3, 3)
print(x)