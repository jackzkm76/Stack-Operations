
class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
            print(f"Pushed: {item}")
        else:
            print("Stack is full! Cannot push.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)

if __name__ == "__main__":
    max_size = 3
    stack = Stack(max_size)
    
    print("Is stack full?", stack.is_full())  

    stack.push(10)  
    stack.push(20) 
    stack.push(30)  
    
    print("Is stack full?", stack.is_full())  

    stack.push(40) 

    stack.display()

    stack.pop()  
    stack.pop() 

    print("Is stack full?", stack.is_full())  
