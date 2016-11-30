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
            def __init__(self, current):
                self.current = current
                self.next = None
            def getCurrent(self):
                return self.current
            def next(self):
                return self.next

        head = Ob(0)
        tmp1 = head
        last = Ob(numRows -1)
        tmp2 = last
        result = ['']

        for i in range(1, numRows -1):
            tmp1.next = Ob(i)
            tmp1 = tmp1.next
            tmp2.next = Ob(numRows - i - 1)
            tmp2 = tmp2.next

            result.append('')

        result.append('')

        tmp1.next = last
        tmp2.next = head
        tmp = head

        for j in range(0, l):
            result[tmp.getCurrent()] += s[j]
            tmp = tmp.next

        return ''.join(result)


def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s,3)

if __name__ == '__main__':
    main()
