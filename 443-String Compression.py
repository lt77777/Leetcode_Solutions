class Solution:
    #T=O(n), S=O(1)
    def compress(self, chars: List[str]) -> int:
		#init slow and fast pointers
        s = f = 0
        n = len(chars)
        
        while f < n:
            #on each iteration the fast pointer would be at a distinct digit
            #slow pointer would be at location where digit value has to be overwritten
            chars[s] = chars[f]
            #init count to 1
            count = 1
            
            #shift fast pointer when we see identical values
            while f+1 < n and chars[f] == chars[f+1]:
                #increment count of current char and shift fast pointer
                count += 1
                f += 1
            
            #if count of current char is greater than 1
            if count > 1:
                #str() op would be O(1) because len(char) < 2000
                #12 should be treated as "1", "2"
                for c in str(count):
                    #in-place update the value
                    chars[s+1]= c
                    #shift slow pointer
                    s += 1
            
            #shift both slow and fast pointers
            f += 1
            s += 1
        #return slow pointer
        return s
    
