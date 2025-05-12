class Solution(object):
	def minEatingSpeed(self, piles, h):
		def valid(piles,eat,h):
			for i in range(len(piles)):
				if h <= 0:
					return False
				ceil = 0
				if piles[i] % eat != 0:
					ceil = 1
				h -= (piles[i] // eat) + ceil
			return (h >= 0)
		left = 1
		right = max(piles)
		solution = right
		while (left <= right):
			mid = (left + right) // 2
			if valid(piles,mid,h) == True:
				solution = min(solution, mid)
				right = mid - 1
			else:
				left = mid + 1
		print(solution)
		return solution


object = Solution()
object.minEatingSpeed([312884470], 312884469)