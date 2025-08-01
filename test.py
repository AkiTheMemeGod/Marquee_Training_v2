class Solution(object):
    def isValid(self, s):
        if not s:
            return False
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values(): 
                stack.append(char)
            elif stack and stack[-1] == mapping[char]:  
                stack.pop()
            else:
                return False
        return not stack
    def longestValidParentheses(self, st):
        l = len(st)
        h = {}
        for i in range(l):
            print(st[i:])
            if self.isValid(st[i:]):
                h[st[i:]] = len(st[i:])
        if not h:
            return 0
        print(h)
s = Solution()
print(s.longestValidParentheses(")()())"))
print(s.isValid("(()"))