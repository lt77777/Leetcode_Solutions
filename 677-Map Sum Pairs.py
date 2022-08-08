class MapSum:

    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        pass

    def sum(self, prefix: str) -> int:
        rtn = 0
        for i in self.map.keys():
            if prefix == i[:len(prefix)]:
                rtn += self.map[i]
        return rtn


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
