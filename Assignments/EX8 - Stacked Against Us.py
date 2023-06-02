STACK_CAPACITY = 40


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.len = 0
      
    def push(self, item):
        if not self.is_full():
            self.list += [item]
            self.len += 1
        else:
            raise NotPossibleError("the stack is full")

    def pop(self):
        if not self.is_empty():
            last = self.list[-1]
            self.list = self.list[:-1]
            self.len -= 1
            return last
        else:
            raise NotPossibleError("the stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise NotPossibleError("the stack is empty")

    def size(self):
        return self.len
        
    def clear(self):
        self.l = []

    def is_full(self):
        return self.len == self.capacity
    
    def is_empty(self):
        return self.len == 0


class WebBrowser:
    def __init__(self):
        self.current_page = "homepage"
        self.history = Stack(STACK_CAPACITY)
        self.visit(self.current_page)

    def visit(self, url):
        try:
            self.current_page = url
            self.history.push(url)
            print(f"You are at {self.current_page}")        
        except NotPossibleError as error:
            raise error

    def back(self):
        if self.history.len > 1:
            self.history.pop()
            self.current_page = self.history.peek()
            print(f"You are at {self.current_page}")        
        else:
            raise NotPossibleError("you've reached home page")
        
    def close(self):
        self.history.clear()

 
class NotPossibleError(Exception):
    pass
