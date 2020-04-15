from LRU import LRU
class LRUTest:
	

	def test(self):
		cacheobj = LRU(3)
		cacheobj.put(1)
		cacheobj.put(2)
		cacheobj.put(3)
		assert cacheobj.get(2) == 2 , "testcase-1 failed"
		print("Testcase-1 passed")
		assert cacheobj.get(3) == 3 , "testcase-1 failed"
		print("Testcase-1 passed")
		print("All test cases are passed")
		print("required cache is:")
		print(cacheobj.get_cache())

if __name__ == "__main__":
	ca = LRUTest()
	ca.test()