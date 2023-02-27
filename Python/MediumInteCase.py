#max even number split
#deduce every even number and add the remained to the last one
#to remain unique
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        else:
            i = 2
            result = []
            while finalSum >= i:
                finalSum -=i
                result.append(i)
                i+=2
                if finalSum <i:
                    result[-1] += finalSum

            return result


                
