#zigzag conversion
#use a row counter to go back and forth between rows in a zigzag way.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <=1:
            return s
        
        result = {row: "" for row in range(numRows)}

        currRow = 0
        up = True
        for letter in s:
            result[currRow] += letter
            if (currRow <numRows -1 and up) or currRow == 0:
                currRow += 1
                up = True
            else:
                currRow -= 1
                up = False
        converted = ""
        for row in range(numRows):
            converted += result[row]
        return converted


       # return the longest common prefix in a list of strings 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) ==0:
            return ""
        else:
            result = ""
            
            begin = min(strs)
            for i in range(len(begin)):
                for s in strs:
                    if i == len(s) or s[i] != begin[i]:
                        return result
                result +=begin[i]
            return result

        
        #write atoi()
        #converte string to int
        class Solution:
    def myAtoi(self, s: str) -> int:
        trimed = s.lstrip()
        #get rid of space
        
        #check if the string is valid
        if not trimed:
            return 0
        
        #parse string and accumulate
        i = 0
        sign = 1
        if trimed[i] == '-':
            sign = -1
            i +=1
        elif trimed[i] == '+':
            i +=1
        result = 0

        while i < len(trimed):
            curr = trimed[i]
            if not curr.isdigit():
                break
            else:
                result = result* 10 + int(curr)
            i +=1

    
        parsed = sign * result
        if parsed > 2**31 -1:
            return 2**31 -1
        elif parsed <= -2**31:
            return -2**31
        else:
            return parsed
