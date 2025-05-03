class Solution(object):
	def minWindow(self, s, t):
		solutionDict = {}
		# populate my s dictionary with t
		for i in range(len(t)):
			solutionDict[t[i]] = solutionDict.get(t[i],0) + 1
		print(solutionDict)
		indexArray = [0] # zero where my window starts
		for i in range(len(s)):
			if s[i] in solutionDict:
				solutionDict
		return