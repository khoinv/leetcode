import sys
sys.path.insert(0,'../')
from common import time_cal

class Solution(object):
    @time_cal
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temps = {}
        for k, num in enumerate(nums):
            x = target - num
            if x in temps:
                return temps[x], k
            else:
                temps[num] = k

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    s1 = Solution()
    print s1.twoSum(nums, 9)
