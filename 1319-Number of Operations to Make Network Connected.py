class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        left = set(range(n))
        edges = defaultdict(lambda : list())
        for con in connections:
            edges[con[0]].append(con[1])
            edges[con[1]].append(con[0])            
        numComponents = 0
                
        while len(left) > 0:
            numComponents += 1
            q = deque([left.pop()])
            while len(q) > 0:
                for nb in edges[q.popleft()]:
                    if nb in left:
                        left.remove(nb)
                        q.append(nb)
        return (numComponents - 1) if (len(connections) >= n-1) else (-1)
        
