class Queue:
    def __init__(self) -> None:
        # Initialize the queue
        self.queue = []

    # Return the size of the queue
    def size(self):
        return len(self.queue)
        
    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Add an element to the queue
    def enqueue(self, element):
        self.queue.append(element)

    # Remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            print("The queue is empty")
            return None
        else:
            return self.queue.pop(0)
            
    # Return the front most element
    def peek(self):
        if self.is_empty():
            print("The queue is empty")
            return None
        else:
            return self.queue[0]
            
    # Display the queue
    def display(self):
        print("Queue elements:", self.queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print("Front element is", queue.peek())
    queue.dequeue()
    queue.display()