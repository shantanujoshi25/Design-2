# // Time Complexity : O(1)
# // Space Complexity : O(m) m is lenght of linkedList
    
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    
    
    
class MyHashMap:


    def __init__(self):
        self.bucket = [ Node(-1,-1) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucketItem = self.getBucketItem(key)
        if(bucketItem.next is None):
            bucketItem.next = Node(key,value)
        else:
            while(bucketItem.next is not None and bucketItem.key != key ):
                bucketItem = bucketItem.next
            if(bucketItem.key == key):
                bucketItem.key = key
                bucketItem.value = value
            else:
                bucketItem.next = Node(key,value)
             

    def get(self, key: int) -> int:
        bucketItem = self.getBucketItem(key)
        if(bucketItem.next is None):
            return -1
        else:
            while(bucketItem.next is not None and bucketItem.key != key ):
                bucketItem = bucketItem.next
            if(bucketItem.key == key):
                return bucketItem.value
            else:
                return -1


    def remove(self, key: int) -> None:
        bucketItem = self.getBucketItem(key)
        if(bucketItem.next is None):
            pass
        elif(bucketItem.next.key == key):
            bucketItem.next = bucketItem.next.next
        else:
            currNode = bucketItem
            nextNode = bucketItem.next
            while(nextNode.next is not None and nextNode.key != key ):
                currNode = nextNode
                nextNode = nextNode.next
            
            if(nextNode.key == key):
                currNode.next = nextNode.next
            else:
                pass

    def getBucketItem(self,key):
        return self.bucket[self.hashing(key)]

    def hashing(self,key):
        return key%1000 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
