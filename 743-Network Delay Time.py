class Node:
    def __init__(self,u,w):
        self.u = u
        self.w = w
    
    def __lt__(self, next): # custom sort based on weight
        return self.w<next.w
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float('inf')]*(n+1)
        distance[k] = 0 # mark distances of each vertice as infinity except the starting node
        
        hashmap = defaultdict(list) # using hashmap to create a adjacency list (can use times array directly but it was confusing)
        
        for time in times:
            hashmap[time[0]].append(time[1:]) # node to neighbors mapping eg-> {2->[1,3]}
        
        nodes = []
        heapq.heappush(nodes, Node(k,0)) # push start vertice as Node where u is the start node and 0 is the distance to visit itself

        while nodes:
            for i in range(len(nodes)):
                curr = heapq.heappop(nodes)

                for neighbor in hashmap[curr.u]:
					# while visiting neighbors of current vertice update the distance of the neighbors 
					#from current vertice(only if the current vertice + neighbors weight is smaller than the exisiting distance)
                    if distance[curr.u]+neighbor[1]<distance[neighbor[0]]:
                        distance[neighbor[0]] = distance[curr.u]+neighbor[1]
                        heapq.heappush(nodes, Node(neighbor[0], neighbor[1]))
		
		# since the question is 1 based indexing distance [0] is always inf
        return -1 if float('inf') in distance[1:] else max(distance[1:])
    
