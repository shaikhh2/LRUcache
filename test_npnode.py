
from npNode import NpNode 
import unittest

class TestnpNodeMethods(unittest.TestCase):

    def test_get(self):
        testNode = NpNode('key1','test1')
        self.assertIsNotNone(testNode.get(), msg='Node should have a data value already set')
        self.assertEquals(testNode.get(), ('key1', 'test1'))


    def test_get_key(self):
        testNode = NpNode('key2','test2')
        self.assertIsNotNone(testNode.get(), msg='Node should have a data value already set')
        self.assertEquals(testNode.get_key(), 'key2')


    def test_get_value(self):
        testNode = NpNode('key3','test3')
        self.assertIsNotNone(testNode.get(), msg='Node should have a data value already set')
        self.assertEquals(testNode.get_value(), 'test3')


    def test_set(self):
        testNode = NpNode('key1', 'test1')
        testValue = 'test2'
        testKey = 'key2'
        print('current value = ', testNode.get())
        testNode.set(testKey, testValue)
        self.assertEquals(testNode.get(), (testKey, testValue))
        print('New value = ', testNode.get())

    def test_set_none(self):
        testNode = NpNode('key', 'value')
        testValue = None
        testKey = None
        print('current value = ', testNode.get())
        testNode.set(testKey, testValue)
        self.assertEquals(testNode.get(), (testKey, testValue))
        print('New value = ', testNode.get())

    def test_set_not_none(self):
        testNode = NpNode(None, None)
        testValue = 'valueNone'
        testKey = 'keyNone'
        print('current value = ', testNode.get())
        testNode.set(testKey, testValue)
        self.assertEquals(testNode.get(), (testKey, testValue))
        print('New value = ', testNode.get())


    def test_hasValueFalse(self):
        testNode = NpNode('key1', 'test1')
        self.assertFalse(testNode.has_value('test2'))
        
    def test_hasValueTrue(self):
        testNode = NpNode('key1', 'test1')
        self.assertTrue(testNode.has_value('test1'))


if __name__ == '__main__':
    unittest.main()
