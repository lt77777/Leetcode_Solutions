class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # the cache is for {old_node: new_node} mapping
        node_cache = {}
        
        # create the new head
        new_head = Node(head.val)
        node_cache[head] = new_head
        
        # This linear scan is for creating a new linked list
        # and create the mapping between old_node and new_node
        node = head
        while node:
            _next = node.next
            if _next:
                new_node = Node(_next.val)
                # Link the new_node
                node_cache[node].next = new_node
                # Store the mapping old_node: new_node
                node_cache[_next] = new_node
                
            node = _next
        
        # This linear scan is for linking the random pointer from
        # mapping.
        node = head
        while node:
            new_node = node_cache[node]
            if node.random:
                # Link the random pointer from cache
                new_node.random = node_cache[node.random]
            node = node.next
            
        return node_cache[head]
