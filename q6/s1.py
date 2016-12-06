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
        class CycleList(object):
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

        cycleList = CycleList(numRows -1)

        lists = [[] for _ in range(0, numRows)]
        for j in s:
            lists[cycleList.next()].append(j)

        # return ''.join((''.join(x) for x in lists)) #> 200
        # return ''.join(itertools.chain.from_iterable(lists)) #> 200
        # return ''.join(sum(lists,[])) #>200
        rs = []
        map(rs.extend,lists)
        return ''.join(rs)


def main():
    s = 'PAYPALISHIRING'
    # s = 'A'
    sl = Solution()
    # sl.convert(s,3)
    print(sl.convert(s,2))

if __name__ == '__main__':
    main()


"""
>>> import itertools
>>> import timeit
>>> big_list = [[0]*1000 for i in range(1000)]
>>> timeit.repeat(lambda: list(itertools.chain.from_iterable(big_list)), number=100)
[3.016212113769325, 3.0148865239060227, 3.0126415732791028]
>>> timeit.repeat(lambda: list(itertools.chain(*big_list)), number=100)
[3.019953987082083, 3.528754223385439, 3.02181439266457]
>>> timeit.repeat(lambda: (lambda b: map(b.extend, big_list))([]), number=100)
[1.812084445152557, 1.7702404451095965, 1.7722977998725362]
>>> timeit.repeat(lambda: [el for list_ in big_list for el in list_], number=100)
[5.409658160700605, 5.477502077679354, 5.444318360412744]
>>> [100*x for x in timeit.repeat(lambda: sum(big_list, []), number=1)]
[399.27587954973444, 400.9240571138051, 403.7521153804846]

with difference input, from_iterable to be faster than map+extend


def append(alist, iterable):
    for item in iterable:
        alist.append(item)

def extend(alist, iterable):
    alist.extend(iterable)
So let's time them:

import timeit

>>> min(timeit.repeat(lambda: append([], "abcdefghijklmnopqrstuvwxyz")))
2.867846965789795
>>> min(timeit.repeat(lambda: extend([], "abcdefghijklmnopqrstuvwxyz")))
0.8060121536254883
We see that extend can run much faster than append
"""
