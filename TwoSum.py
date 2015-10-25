class Solution(object):
	def twoSumd(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		ntarget = target
		if target == 0:
			target = 1
		if target < 0:
			target = 0 - target
		t = [None] * target
		for k, v in enumerate(nums):
			h = v % target
			if h < 0:
				h = target + h
			g = (target - v) % target
			if g < 0:
				g = target + hs
			if t[h] == None:
				 t[h] = dict()
			if t[g] != None:
				for (m, n) in t[g].items():
					if ntarget == v + n:
						print("index1=%d, index2=%d" % (m+1, k+1))
						return (m+1, k+1)
			t[h][k] = v