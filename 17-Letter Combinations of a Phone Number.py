class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not isinstance(digits, str) or len(digits)==0:
            return []
        
        mapping = {2:['a','b','c'], 3:['d','e','f'],
        4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
        7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        
        if len(digits)==1:
            return mapping[int(digits[0])]
        
        return list(map(lambda y:''.join(y), 
                itertools.product(*[mapping[int(x)] for x in digits])))
