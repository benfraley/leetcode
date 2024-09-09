# https://neetcode.io/problems/validate-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            # a closing paren has to have its opener at the end of the stack
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
        return True if not stack else False
