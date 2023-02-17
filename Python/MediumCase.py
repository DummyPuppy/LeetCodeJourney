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
                
#mine sweeper
#soooo difficult
#consider three cases and need a helper method
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        r = click[0]
        c = click[1]
        n = len(board[0])
        m = len(board)
        def AdjacentMines(x,y):
            count = 0
            if board[x][y] == 'E':
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if (i >=0 and i < m) and (j >=0 and j < n):
                            print(i,j)
                            if board[i][j] == 'M':
                                count +=1
            return count
                        
                

        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            if board[r][c] =='E':
                count = AdjacentMines(r,c)
                if count != 0:
                    board[r][c] = str(count)
                else:
                    board[r][c] = 'B'
                    for i in range(r-1,r+2):
                        for j in range(c-1,c+2):
                            if (i >=0 and i < m) and (j >=0 and j < n) \
                            and board[i][j] != 'B':
                                self.updateBoard(board,[i,j])
        
        return board
        

    
#this is the weirdest medium case
#find three consecutive nums to sum up to k
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = int(num/3)
        if mid-1 + mid + mid+1 == num:
            return [mid-1, mid, mid+1]
        else: 
            print(mid)
            return []
