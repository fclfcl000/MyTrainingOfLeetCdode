class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		len1 = len(nums1)
		len2 = len(nums2)
		slice = int((len1 + len2) / 4)
		print(nums1)
		print(nums2)
		print("---")
		if slice == 0:
			nums = sorted(nums1 + nums2)
			if len(nums) == 1:
				return nums[0]
			elif len(nums) == 2:
				return (nums[0] + nums[1]) / 2.0
			else:
				return nums[1]
		
		if len1 < slice:
			nums2 = nums2[slice : len2 - slice]
		elif len2 < slice:
			nums1 = nums1[slice : len1 - slice]
		elif len1 == len2:
			if nums1[slice -1] < nums2[slice - 1]:
				nums1 = nums1[slice:]
				len1 = len(nums1)
			else:
				nums2 = nums2[slice:]
				len2 = len(nums2)
			if nums1[len1 - slice] > nums2[len2 - slice]:
				nums1 = nums1[:len1 - slice]
			else:
				nums2 = nums2[:len2 - slice]			
			return self.findMedianSortedArrays(nums1, nums2)
		else:
			if len2 > len1:
				nums1, nums2 = nums2, nums1
			len1 = len(nums1)
			len2 = len(nums2)
			print (nums1)
			print (nums2)
			print ("+++++++")
			if nums1[slice - 1] <= nums2[slice - 1]:
				nums1 = nums1[slice:]
				len1 = len(nums1)
				if nums1[len1 - slice] >= nums2[len2 - slice]:
					print (nums1)
					print (nums2)
					print ("+++++++")
					nums1 = nums1[:len1 - slice]
				else:
					
					nums2 = nums2[:len2 - slice]
			else:
				nums1 = nums1[:len1 - slice]
				nums2 = nums2[slice:]
		return self.findMedianSortedArrays(nums1, nums2)	
		