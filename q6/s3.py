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

        l = len(s)
        tmps = []
        lists = []
        for i in range(0,numRows):
            lists.append([])
            tmps.append(i)

        for i in range(1,numRows -1):
            tmps.append(numRows - i -1)

        for j in s:
            lists[tmps[0]].append(j)
            tmps = np.roll(tmps,-1)

        return ''.join((''.join(x) for x in lists))


def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s, 3)


if __name__ == '__main__':
    main()
