import xlrd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

import django
django.setup()
from main.models import Express
import django.utils.timezone as timezone
import random
import re



b = list(range(1, 101))
counter = 0
c = []
curMax = 100
while len(b) > 1:
    d = 0
    while d < 7:
        counter += 1
        if counter > curMax:
            counter = counter - curMax
        if counter not in c:
            d += 1
    
    c.append(counter)
    b.remove(counter)
    curMax = max(b)

# print(c, b)
# for i in range(1, 101):
#     if i not in c:
#         print(i)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for each in nums:
            each = abs(each) - 1
            nums[each] = -abs(nums[each])
            
        return (i+1 for i, each in enumerate(nums) if each > 0)

# l = [4,3,2,7,8,2,3,1]
# o = Solution()
# result = o.findDisappearedNumbers(l)
# result = list(result)
# print(result)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i, each in enumerate(nums):
            if each != 0:
                nums[x], nums[i] = nums[i], nums[x]
                x += 1

# l = [0, 1, 0, 3, 0, 0, 0, 1, 2, 3, 12]
# o = Solution()
# result = o.moveZeroes(l)
# print(l)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

numbers = [2, 7, 11, 15];target = 9
o = Solution()
result = o.moveZeroes(l)
print(l)