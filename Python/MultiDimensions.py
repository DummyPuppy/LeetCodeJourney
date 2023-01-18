#merge intervals
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
        
        goal = len(nums)-1
        for i in range(len(nums)-2, -1,-1):
            if i+nums[i] >=goal:
                goal = i
        return True if goal == 0 else False

    
  #insert intervals
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()
        for i in range(len(intervals)):
            temp = intervals[i]
            if newInterval[1] < temp[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > temp[1]:
                result.append(temp)
            else: 
                newInterval = [min(newInterval[0],temp[0]),max(newInterval[1],temp[1])]
        result.append(newInterval)
        return result
            
        
        
    #unique paths across a matrix
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [[0 for i in range(n)] for k in range(m)]
        steps[0][0] = 1
        for i in range(m):
            steps[i][0] = 1
        for j in range(n):
            steps[0][j] = 1
        for k in range(1,m):
            for l in range(1,n):
                steps[k][l] = steps[k-1][l] + steps[k][l-1]
        return steps[m-1][n-1]
        
            
                
