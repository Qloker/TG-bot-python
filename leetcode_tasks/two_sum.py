'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        for index1 in range(0, len(nums)):
            for index2 in range(0, len(nums)):
                if (nums[index1] + nums[index2] == target) and (index1 != index2):
                    return [index1, index2]

l1 = [1, 3, 5, 2]
t = 3

for index1 in range(0, len(l1)):
    for index2 in range(0, len(l1)):
        if (l1[index1] + l1[index2] == t) and (index1 != index2):
            print(index1, index2)