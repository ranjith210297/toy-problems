class LRU:
	def _init_(self,size):
		self.size = size
		self.lru = []
		self.lrucache = {}