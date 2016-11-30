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
        class Node(object):
            def __init__(self, current):
                self.current = current
                self.next = None
            def getCurrent(self):
                return self.current
            def next(self):
                return self.next

        head1 = Node(0)
        tmp1 = head1
        head2 = Node(numRows -1)
        tmp2 = head2
        result = ['','']

        for i in range(1, numRows -1):
            tmp1.next = Node(i)
            tmp1 = tmp1.next
            tmp2.next = Node(numRows - i - 1)
            tmp2 = tmp2.next

            result.append('')

        tmp1.next = head2
        tmp2.next = head1

        tmp = head1

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
