class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            sol = Solution()
            rec = 2*n + 2*(n-2)
            rec2 = sol.coloredCells(n-1)
            rec = rec2 + rec
            return rec

        
