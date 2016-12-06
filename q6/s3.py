import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        lists = [[] for _ in range(0, numRows)]
        cycleList = [i for i in range(0, numRows)]

        for i in range(1,numRows -1):
            cycleList.append(numRows - i -1)

        for j in s:
            lists[cycleList[0]].append(j)
            cycleList = np.roll(cycleList, -1)

        rs = []
        map(rs.extend,lists)
        return ''.join(rs)

def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s, 3)


if __name__ == '__main__':
    main()
