class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
class LRUCache:
    def __init__(self, MAX_CAPACITY):
        self.MAX_CAPACITY = MAX_CAPACITY
        self.cache = {}

        head = Node(None,None) # Head is the most recent
        tail = Node(None,None) # Tail is the least recent

        self.head.next = tail
        self.tail.prev = head

    def get(self, key: int) -> int: # @Param the key for the cache @Return returns the value from the node inside the cache
        if key in self.cache:
            self.move_to_front(self.cache[key])
            return self.cache[key].value
        return -1
    '''
        sets the node(inside the given cache key)'s value to value if the key already exists. 
        otherwise, calls on add_node_at_front which then calls on evict_lru.
        no need to call evict_lru if the key already exists, because no new node is added
    '''
    def put(self, key: int, value) -> None: 
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_front(get(key))
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_node_at_front(new_node)
    
    def move_to_front(self, node: Node) -> None: # @Param node is moved to the front of the LL
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
    

    def remove_node(self, node: Node) -> None: # @Param removes given node from LL
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node_at_front(self, node: Node) -> None: # @Param adds a node to the top of the LL, then calls evict_lru
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.evict_lru()

    def evict_lru(self) -> None: # removes cache keys and corresponding nodes if they are over the max_capacity and at the end of the LL
        if len(self.cache) > self.MAX_CAPACITY:
            self.cache.pop(self.tail.prev.key)
            self.remove_node(self.tail.prev)