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
