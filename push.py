
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def display(self):
        if not self.items:
            print("Stack is empty.")
        else:
            print("Stack items:", self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10) 
    stack.push(20) 
    stack.push(30) 
    
    stack.display()