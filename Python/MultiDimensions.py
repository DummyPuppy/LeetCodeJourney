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
            
