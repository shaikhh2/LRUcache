from lruCache import LRUCache


def printCache(cacheToPrint):
    print('\n\n')
    print('Current state of cache (with LRU value at bottom):')
    curr = cacheToPrint.head
    while curr:
        print (f'|key: {curr.get_key()} Value: {curr.get_value()}|')
        curr = curr.next
    print('\n\n')

testCache = LRUCache(5)
testCache.put('myString', 'myStringValue')
testCache.put(1,1)
testCache.put(1,'string1')
testCache.put(None, None)
testCache.put('stringkey', 1)
testCache.put('mykey', 1.4)
testCache.put('testkey', 'testvalue')

printCache(testCache)
print(f'testCache.get(1) {testCache.get(1)}')

print(f'testCache.delete(1) {testCache.delete(1)}\n\n')
printCache(testCache)

print(f'testCache.reset() {testCache.reset()}')
printCache(testCache)



