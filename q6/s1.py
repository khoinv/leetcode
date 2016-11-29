import collections
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
        class Ob(object):
            def __init__(self, m):
                self.current = 0
                self.increatement = 1
                self.max = m
                self.tmp = 0

            def next(self):
                self.tmp = self.current
                self.current += self.increatement
                if(self.current == self.max or self.current == 0):
                    self.increatement = -self.increatement
                return self.tmp

        a = Ob(numRows -1)


        dic = collections.defaultdict(list)
        j = 0
        while j < l:
            dic[a.next()].append(s[j])
            j += 1

        result = []
        for i in range(0, numRows):
            result.append(''.join(dic[i]))


def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s,3)

if __name__ == '__main__':
    main()