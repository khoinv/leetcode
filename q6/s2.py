class Node(object):
    def __init__(self, current):
        self.current = current
        self.next = None

    def next(self):
        return self.next

def createCycleLinkedList(numRows):
        head = Node(0)
        tmp = head
        recusive_head = Node(numRows - 1)
        rtmp = recusive_head

        for i in range(1, numRows - 1):
            tmp.next = Node(i)
            tmp = tmp.next
            rtmp.next = Node(numRows - i - 1)
            rtmp = rtmp.next

        tmp.next = recusive_head
        rtmp.next = head

        return head


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if len(s) <= numRows:
            return s

        cycleList = createCycleLinkedList(numRows)
        lists = [[] for _ in range(0, numRows)]

        for j in s:
            lists[cycleList.current].append(j)
            cycleList = cycleList.next

        rs = []
        map(rs.extend,lists)
        return ''.join(rs)

def main():
    s = 'PAYPALISHIRING'
    sl = Solution()
    sl.convert(s, 3)


if __name__ == '__main__':
    main()
