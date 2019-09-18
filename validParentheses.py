left = ('(', '[', '{')
m = {')':'(', '}':'{', ']':'['}
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            else:
                ans = m[char]
                if not stack:
                    return False
                if ans == stack.pop():
                    continue
                else:
                    return False
        return len(stack) == 0
