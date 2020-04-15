
import LRU
class LRUTest:
	cacheobj = LRU()
	cacheobj.get()
	cacheobj.put(item1)
	cacheobj.put(item2)
	cacheobj.put(item3)

	cacheobj.get_cache()



assert("suucessful",cacheobj.put(1))
assert("suucessful",cacheobj.put(2))
assert("suucessful",cacheobj.put(3))
assert("1",cacheobj.get())
assert("3".cacheobj.get_cache())
print("All test cases are passed")