# class Solution(object):
#     def containsDuplicate(self, nums):
#         di={}
#         for i in range(len(nums)):
#             if nums[i] in di:
#                 return True
#             else:
#                 di[nums[i]]=i
#         return False        
        
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False                   
