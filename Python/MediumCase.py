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


      
      
