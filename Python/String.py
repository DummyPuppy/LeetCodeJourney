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


        
