from math import sqrt 
def seive():
    _max = int(5* 1e6)+1 
    primes = [True]*_max  
    primes[0] = False 
    primes[1] = False 
    for i in range(2,int(sqrt(_max)+1)):
        if primes[i]:
            for j in range(i*i,
             _max,i):
                primes[j] = False 
    return primes 


primes = seive() 

class Solution:
    def countPrimes(self,n):
        count = 0 
        for i in range(n):
            if primes[i]:
                count+=1 
        return count 
