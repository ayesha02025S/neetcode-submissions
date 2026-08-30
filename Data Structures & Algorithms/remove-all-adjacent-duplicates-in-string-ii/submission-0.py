class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # char, count 

        for c in s:
            if stack and stack[-1][0] == c: # top of the stack - first of the pair (char)
                stack[-1][1] +=1 # increment the count
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += (char * count)
        
        return res
            

        