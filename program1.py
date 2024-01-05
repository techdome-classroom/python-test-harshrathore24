from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = LifoQueue()
        for i in s:
            if i in {'}',']',')'} and stack.empty() == True:
                return False
            if i in {'(', '{' , '['}:
                stack.put(i)
            if i in {')'}:
                if stack.queue[-1] == '(':
                    stack.get()
                else:
                    return False
            if i in {']'}:
                if stack.queue[-1] == '[':
                    stack.get()
                else:
                    return False
            if i in {'}'}:
                if stack.queue[-1] == '{':
                    stack.get()
                else:
                    return False

        if stack.empty() == True:
            return True
        else:
            return False