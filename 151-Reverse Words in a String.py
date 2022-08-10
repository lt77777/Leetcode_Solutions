class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split() #split the string, so the result will be a list with list[i] == word
        reversed_str = [] #create an empty list
        for i in reversed(splitted): #for in our splitted list starting from the end
            reversed_str.append(i) #append the word we're traversing (reversed) to our reversed_str list
        return " ".join(reversed_str) #return the joined reversed string
    
