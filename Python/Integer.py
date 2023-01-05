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
