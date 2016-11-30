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

        # TODO: create new cycle list
        # class Node(object):
        #     def __init__(sefl, m):
        #         self.current = m
        #         self.next = None

        #     @property
        #     def next(self):
        #         return self.next

        #     @next.setter
        #     def next(self, node):
        #         self.next = node

        a = Ob(numRows -1)


        dic = collections.defaultdict(list)
        j = 0
        for j in range(0, l):
            dic[a.next()].append(s[j])

        result = []
        for i in range(0, numRows):
            result.append(''.join(dic[i]))
        return ''.join(result)


def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s,3)

if __name__ == '__main__':
    main()
