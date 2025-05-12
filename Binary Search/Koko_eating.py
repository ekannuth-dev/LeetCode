class Solution(object):
	#def binarySearch(array, left, right):
	#	mid = left + right // 2
	def valid(piles,eat,h):
		for i in range(len(piles)):
			if h <= 0:
				return False
			print(piles // eat)
			print(piles % eat)
			h -= piles // eat + piles % eat
		return True

	def minEatingSpeed(self, piles, h):
		end = max(piles)
		binarySearch = [1]
		for i in range(2,end+1):
			binarySearch += [i]
		# created array to run binarySearch
		print(binarySearch)
		self.valid(piles,piles[i],h)
		#think about one value for now
		return


object = Solution()
object.minEatingSpeed([1,2], 8)