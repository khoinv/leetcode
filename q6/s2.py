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
                self._current = current
                self.next = None

            def current(self):
                return self._current

            def next(self):
                return self.next

        head = Node(0)
        tmp = head
        recusive_head = Node(numRows - 1)
        rtmp = recusive_head
        result = ['', '']

        for i in range(1, numRows - 1):
            tmp.next = Node(i)
            tmp = tmp.next
            rtmp.next = Node(numRows - i - 1)
            rtmp = rtmp.next

            result.append('')

        tmp.next = recusive_head
        rtmp.next = head

        tmp = head

        for j in range(0, l):
            result[tmp.current()] += s[j]
            tmp = tmp.next

        return ''.join(result)


def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s, 3)


if __name__ == '__main__':
    main()
