
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

    def is_empty(self):
       
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)  
    stack.push(20)  
    stack.push(30)  
    
  
    stack.display()

  
    stack.pop() 
    stack.pop()  
    stack.pop() 
    stack.pop()  