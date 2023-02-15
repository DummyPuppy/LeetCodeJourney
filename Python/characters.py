#check valid parentheses
#use stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'[':']','(':')',"{":"}"}

        for ch in s:
            if ch in map.keys():
                stack.append(ch)
            elif not stack or map[stack.pop()] != ch:
                return False
        return not stack
            
