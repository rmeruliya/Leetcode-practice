class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        stack = []
        #using hashmap to check if the closing braces match the opening bracses
        hashmap = {')' : '(', ']':'[','}':'{'}
       
        for i in s:
            #we check if the closing braces(key) is in hashmap 
            if i in hashmap:
                #we check if the value of closing braces(hashmap value of key) is matching last value of stack and also checking if stack is not empty(if stack)
                if stack and stack[-1] == hashmap[i]:
                    #if value is equal we remove from stack
                    stack.pop()
                else:
                    #otherwise false
                    return False
            else:
                #if its and opening braces it would not be found in hashmap and it would append it to stack
                stack.append(i)
        #returns true if stack is empty(if not stack) other wise if stack contains value it returns false        
        return True if not stack else False
          