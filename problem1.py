# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if (nums[i]+nums[j]==target):
#                     return i,j


class Solution(object):
    def twoSum(self, nums, target):
        di={}
        for i in range(len(nums)):
            if not target-nums[i] in di:
                di[nums[i]]=i
            else:
                return i,di[target-nums[i]]    





