class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:]=nums1[:m]
        nums1.extend(nums2[:n])

        for i in range(m+n-1):
            for j in range(m+n-i-1):
                if(nums1[j]>nums1[j+1]):
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]       
        
