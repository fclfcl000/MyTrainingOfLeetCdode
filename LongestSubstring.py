class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max = 0

		for v in s:
			if ord(v) > max:
				max = ord(v)
		
		f = [-1 for k in range(max + 1)]

		max = 0
		pre_max = 0
		for k, v in enumerate(s):
			if pre_max < (k - f[ord(v)]):
				len = pre_max + 1
			else:
				len = k - f[ord(v)]
			
			if len > max:
				max = len
			f[ord(v)] = k
			pre_max = len
		return max