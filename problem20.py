class Solution(object):
    def isValid(self, s):
        characters={
            "]":"[",
            "}":"{",
            ")":"("}
        stack=[]


        for i in s:
            if i in characters:
                if stack:
                    top_element=stack.pop()
                return False    
                
                if top_element!=characters[i]:
                    return False
            else:
                stack.append(i)
            
        return not stack
