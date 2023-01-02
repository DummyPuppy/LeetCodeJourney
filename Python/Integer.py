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
            if result < -2**32 or result > 2**32-1 :
                return 0
        if x < 0 :
            return result * (-1)
        else:
            return result
