from lruCache import LRUCache
from npNode import NpNode
import unittest

class TestLRUCacheMethods(unittest.TestCase):

    def setUp(self):
        self.testCache = LRUCache(5)
        self.testCache.put('myString', 'myStringValue')
        self.testCache.put(1,1)
        self.testCache.put(1,'string1')
        self.testCache.put(None, None)
        self.testCache.put('stringkey', 1)
        self.testCache.put('mykey', 1.4)
        
        self.testcache2 = LRUCache(3)

    def test_get(self):
        self.assertEquals(self.testCache.get('myString'), 'myStringValue')
        self.assertEquals(self.testCache.get(1), 'string1')
        self.assertEquals(self.testCache.get('stringkey'), 1)
        self.assertIsNone(self.testCache.get('1'))
        self.testcache2.put(-1,-2)
        self.assertEquals(self.testcache2.get(-1), -2)



    def test_put(self):
        self.testcache2.put(1,1)
        self.testcache2.put(2,2)
        self.testcache2.put(3,3)
        self.testcache2.put(4,4)

    def test_delete(self):
        self.testCache.delete(1)
        self.assertIsNone(self.testCache.get(1))

    def test_delete_tail(self):
        self.testCache.delete('myString')
        self.assertIsNone(self.testCache.get('myString'))

    def test_delete_head(self):
        self.testCache.delete('mykey')
        self.assertIsNone(self.testCache.get('mykey'))

    def test_delete_singleNodeQueue(self):
        self.testcache2.put(1,1)
        self.testcache2.delete(1)
        self.assertFalse(self.testcache2.dict)
        self.assertIsNone(self.testcache2.head)
        self.assertIsNone(self.testcache2.tail)
        self.assertEquals(self.testcache2.maxsize, 3)
        
    def test_reset(self):
        self.testcache2.reset()
        self.assertFalse(self.testcache2.dict)
        self.assertIsNone(self.testcache2.head)
        self.assertIsNone(self.testcache2.tail)
        self.assertEquals(self.testcache2.maxsize, 3)


if __name__ == '__main__':
    unittest.main()
