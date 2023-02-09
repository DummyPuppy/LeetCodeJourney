#container with the most water
#o(n) run time 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n <=1:
            return 0
        left_idx =0
        right_idx = n-1
        mostwater = 0
        
        while left_idx< right_idx:
            volume = (right_idx - left_idx) * min(height[left_idx],height[right_idx])
            if volume > mostwater:
                mostwater = volume
            if height[left_idx] > height[right_idx]:
                right_idx -=1
            else:
                left_idx +=1
        return mostwater


      
      #letter combo of digits
    #use stack to store the previous combos till the full ones
    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        
        map = dict()
        map['2'] = ['a','b','c']
        map['3'] = ['d','e','f']
        map['4'] = ['g','h','i']
        map['5'] = ['j','k','l']
        map['6'] = ['m','n','o']
        map['7'] = ['p','q','r','s']
        map['8'] = ['t','u','v']
        map['9'] = ['w','x','y','z']
        stack = [(0,'')]
        combo = []
        while stack:
            idx, char = stack.pop()
            if idx == len(digits):
                combo.append(char)
            else:
                for letter in map[digits[idx]]:
                    stack.append((idx+1, char + letter))
        return combo
                
