from functools import *

class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		mpos = 0
		mlen = 0
		ss = '\0' + reduce(lambda x, y: x + '\0' + y, s) + '\0'
		L = [0 for i in ss]
		for (i, v) in enumerate(ss):
			brother = 2 * mpos - i
			if i >= mpos + mlen:
				L[i] = 0
			elif mpos + mlen - i > L[brother]:
				L[i] = L[brother]
			elif mpos + mlen - i <= L[brother]:
				L[i] = mpos + mlen - i
			
			j = L[i]
			while i >= j + 1 and i < len(ss) - j - 1 and ss[i - j - 1] == ss[i + j + 1]:
				j = j + 1

			L[i] = j
			if L[i] >= mlen:
				mpos = i
				mlen = L[i]
		return ''.join(filter(lambda x: x != '\0', ss[mpos - mlen:mpos + mlen + 1]))