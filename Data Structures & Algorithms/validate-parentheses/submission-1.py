class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}
        # iterate through string
        for char in s: 
            # check if char is a close bracket
            if char in closeToOpen:
                # check if stack is non empty and top of stack is 
                # coresponding opening
                if stack and stack[-1] == closeToOpen[char]:
                    # remove bracket
                    stack.pop()
                # if not coresponding opening
                else:
                    return False
            # if opening, add to stack
            else: 
                stack.append(char)
        # return true if stack is empty, otherwise false 
        return True if not stack else False
            