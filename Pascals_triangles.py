class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows ==1:
            output = []
            output.append([1])
            return output
        elif numRows ==2:
            output = [[1]]
            output.append([1,1])
            return output
        elif numRows <=0:
            output = []
            return output
        else:
            solution_object = Solution()
            output = solution_object.generate(numRows-1)
            last_piece = output[-1]
            x = [1]
            for i in range (numRows-2):
                x.append(last_piece[i]+last_piece[i+1])
            x.append (1)
            output.append(x)
            return output




        
