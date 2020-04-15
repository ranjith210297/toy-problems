class LRU:
	def __init__(self, size):
		self.size = size
		self.lru = []
		self.lrucache = {}


	def get(self,item,default = None):
		if item in self.lru:
			return self.lrucache[item]
		else:
			return default

	def put(self,item):
		if(len(self.lru) < self.size):
			if item in self.lru:
				self.lru.remove(item)
				self.lru.append(item)
				self.lrucache[item] = item
			else:
				self.lru.append(item)
				self.lrucache[item] = item
			return "Successful"

		else:
			var = self.lru.pop()
			self.lru.append(item)
			del self.lrucache[var]
			self.lrucache[item] = item
			return "Successful"

	def get_cache(self):
		ls = []
		for item in reversed(self.lru):
			ls.append(str(item)+"-"+str(self.lrucache[item]))
		#return get-cache
		print(ls)