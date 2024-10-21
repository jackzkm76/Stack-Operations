
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            top_item = self.items[-1]
            print(f"Top item: {top_item}")
            return top_item
        else:
            print("Stack is empty! No top item.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.peek()  

    stack.push(10)  
    stack.push(20) 
    stack.push(30)  

    stack.display()

    stack.peek() 

    
    stack.pop()  
    stack.peek() 
    