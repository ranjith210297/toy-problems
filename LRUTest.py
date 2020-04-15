import LRU
class LRUTest:
	cacheobj = LRU(3)
	cacheobj.get()
	cacheobj.put(1)
	cacheobj.put(2)
	cacheobj.put(3)

	cacheobj.get_cache()



# assert("suucessful",cacheobj.put(1))
# assert("suucessful",cacheobj.put(2))
# assert("suucessful",cacheobj.put(3))
# assert("1",cacheobj.get())
# assert("3".cacheobj.get_cache())
# print("All test cases are passed")