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
        # for i, each in enumerate(numbers):
        #     r = len(numbers) - 1
        #     l = i + 1
        #     tar = target - each
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if numbers[mid] == tar:
        #             return [i+1, mid+1]
        #         elif numbers[mid] < tar:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        l, r = 0, len(numbers) - 1
        while l < r:
            lr = numbers[l] + numbers[r]
            if lr == target:
                return [l+1, r+1]
            elif lr < target:
                l += 1
            else:
                r -= 1


# l = [2, 7, 3, 5, 34, 8, 12, 43, 11, 15];target = 54
# o = Solution()
# result = o.twoSum(l, target)
# print(result)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for each in nums:
            if count == 0:
                major = each
                count += 1
            elif major == each:
                count += 1
            else:
                count -= 1
        return major
    
# l = [2, 7, 3, 5, 34, 3, 3, 3, 11, 15]
# o = Solution()
# result = o.majorityElement(l)
# print(result)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = list(set(nums))
        print(nums, nums2)
        return nums != nums2

l = [3, 1]
o = Solution()
result = o.containsDuplicate(l)
print(result)