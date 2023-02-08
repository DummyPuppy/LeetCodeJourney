//reverse integer and assign the correct sign

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        temp = 0
        y = abs(x)
        while y != 0:
            temp = y % 10
            result  = (result * 10) + temp
            y = y//10
        if result < -2**31 or result > 2**31-1 :
            return 0
        else:
            if x < 0:
                return result *-1
            else:
                return result

   
#find three int that sum up to 0
#exceed time limit
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        pos = []
        neg =[]
        zero =[]
        nums.sort()
        for num in nums:
            if num > 0:
                pos.append(num)
            if num == 0:
                zero.append(num)
            if num < 0 :
                neg.append(num)
        #for zeros
        if len(zero) >= 3:
            result.add((0,0,0))
        #for pos and neg
        if len(zero) > 0:
            setneg = set(neg)
            setpos = set(pos)
            for i in setneg:
                if -1*i in setpos:
                    result.add((i,0,-1*i))
        #for two neg
        for k in range(len(neg)):
            for j in range(k+1, len(neg)):
                target =  -neg[k]-neg[j]
                if target in pos:
                    result.add((neg[k],neg[j],-neg[k]-neg[j]))
        #for two pos
        for m in range(len(pos)):
            for n in range(m+1, len(pos)):
                target =  -pos[m]-pos[n]
                if target in neg:
                    result.add((pos[m],pos[n],-pos[m]-pos[n]))
        return result

    
    #solution
    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        pos = []
        neg =[]
        zero =[]
        nums.sort()
        for num in nums:
            if num > 0:
                pos.append(num)
            if num == 0:
                zero.append(num)
            if num < 0 :
                neg.append(num)
        #for zeros
        if len(zero) >= 3:
            result.add((0,0,0))
        #for pos and neg
        setneg = set(neg)
        setpos = set(pos)
        if len(zero) > 0:
            for i in setneg:
                if -1*i in setpos:
                    result.add((i,0,-1*i))
        #for two neg
        for k in range(len(neg)):
            for j in range(k+1, len(neg)):
                target =  -neg[k]-neg[j]
                if target in setpos:
                    result.add((neg[k],neg[j],target))
        #for two pos
        for m in range(len(pos)):
            for n in range(m+1, len(pos)):
                target =  -pos[m]-pos[n]
                if target in setneg:
                    result.add((pos[m],pos[n],target))
        return result

    
    #spiral traversal
    class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        leftbound = 0
        rightbound = len(matrix[0])
        lowerbound = len(matrix)
        upperbound = 0

        while leftbound < rightbound and upperbound < lowerbound:
            for i in range(leftbound,rightbound):
                result.append(matrix[upperbound][i])
            upperbound +=1
            for j in range(upperbound, lowerbound):
                result.append(matrix[j][rightbound-1])
            rightbound -=1

            if not (leftbound < rightbound and upperbound < lowerbound):
                break
            

            for i in range(rightbound-1,leftbound - 1, -1):
                result.append(matrix[lowerbound-1][i])
            lowerbound -=1
            for j in range(lowerbound-1,upperbound-1,-1):
                result.append(matrix[j][leftbound])
            leftbound +=1
        return result
    
    
    #spiral insertion
    class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n
        top = 0
        bottom = n
        pos = 1
        mat = [[0]* n for i in range(n)]
        while (left < right and top < bottom):
            for i in range(left,right):
                mat[top][i] = pos
                pos+=1
            top+=1

            for j in range(top,bottom):
                mat[j][right-1] = pos
                pos+=1
            right-=1

            if not (left < right and top < bottom):
                break
            for k in range(right-1,left-1 ,-1):
                mat[bottom-1][k] = pos
                pos+=1
            bottom-=1
            
            for m in range(bottom-1,top-1,-1):
                mat[m][left] = pos
                pos+=1
            left+=1
            
            
        return mat

            
            
#find palidrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s) % 2 ==0:
            l = len(s)/2
        else:
            l = (len(s)-1)/2
        print(l)
        for i in range(int(l)):
            if s[i] != s[len(s)-i-1]:
                return False
            
        return True

  #convert integer to roman letter
class Solution:
    def intToRoman(self, num: int) -> str:
        if num <=0:
            return ''
        
        answer = ''

        map = dict()
        map[1] = 'I'
        map[4] = 'IV'
        map[5] = 'V'
        map[9] = 'IX'
        map[10] = 'X'
        map[40] = 'XL'
        map[50] = 'L'
        map[90] = 'XC'
        map[100] = 'C'
        map[400] = 'CD'
        map[500] = 'D'
        map[900] = 'CM'
        map[1000] = 'M'
        print(map)
        for key, value in reversed(map.items()):
            if num // key:
                count = num //key
                answer += count * value
                num = num % key

        return  answer


            
