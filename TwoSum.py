class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k, i in enumerate(nums):
            for z, j in enumerate(nums[k+1:]):
				if target == i + j:
					print "index1=%d, index2=%d" % (k + 1, k + 1 + z + 1)
					return