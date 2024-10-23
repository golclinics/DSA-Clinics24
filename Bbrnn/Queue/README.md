# Queue: Data Structure Overview

A **Queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle, meaning the first element added to the queue is the first one to be removed. Queues are widely used in various systems such as scheduling, buffering, and resource management.

## Table of Contents

- [What is a Queue?](#what-is-a-queue)
- [Operations on a Queue](#operations-on-a-queue)
- [Applications of Queue](#applications-of-queue)
- [Pseudocode and Example Implementation](#pseudocode-and-example-implementation)
- [Advantages of Queue](#advantages-of-queue)
- [Limitations of Queue](#limitations-of-queue)

---

## What is a Queue?

A **Queue** is an abstract data type (ADT) that stores a collection of elements and allows for two main operations: **enqueue** and **dequeue**. The queue operates on the **FIFO (First In, First Out)** principle, where the first item inserted is the first one to be removed.

An everyday example of a queue is a line of people waiting for a service: the first person in line is the first one served, and new arrivals join at the back of the line.

---

## Operations on a Queue

A queue typically supports the following operations:

1. **Enqueue**: Adds an element to the end (rear) of the queue.
   - **Pseudocode**:
     ```text
     Enqueue(queue, element):
       if queue is full:
           return "Queue Overflow"
       else:
           increment rear
           queue[rear] = element
     ```

2. **Dequeue**: Removes and returns the element at the front of the queue.
   - **Pseudocode**:
     ```text
     Dequeue(queue):
       if queue is empty:
           return "Queue Underflow"
       else:
           element = queue[front]
           increment front
           return element
     ```

3. **Peek (Front)**: Returns the front element without removing it from the queue.
   - **Pseudocode**:
     ```text
     Peek(queue):
       if queue is empty:
           return "Queue is empty"
       else:
           return queue[front]
     ```

4. **IsEmpty**: Checks if the queue is empty.
   - **Pseudocode**:
     ```text
     IsEmpty(queue):
       if front == rear + 1:
           return True
       else:
           return False
     ```

5. **IsFull**: Checks if the queue is full (relevant for fixed-size implementations).
   - **Pseudocode**:
     ```text
     IsFull(queue):
       if rear == max_size - 1:
           return True
       else:
           return False
     ```

---

## Applications of Queue

Queues are essential in various computing scenarios, including:

### 1. **CPU Scheduling**
   - **Description**: Operating systems use queues to schedule processes. For example, jobs are queued up in the CPU scheduler, and the CPU processes them in the order they arrive (FIFO).

### 2. **Resource Management (Printer Spoolers, Disk Scheduling)**
   - **Description**: In resource management, queues are used to manage tasks like print jobs where jobs are completed in the order they are submitted.

### 3. **Data Buffering**
   - **Description**: Queues are used for buffering data in IO systems (e.g., in a network where data packets are processed in the order they are received).

### 4. **Breadth-First Search (BFS)**
   - **Description**: In BFS algorithms for graph traversal, queues are used to explore nodes level by level in the order they were visited.

### 5. **Asynchronous Data Transfer (Messaging Queues)**
   - **Description**: Queues are used in messaging systems (e.g., Amazon SQS) where producers generate messages, and consumers process these messages later in the order they arrive.

---

## Pseudocode and Example Implementation

Here’s a simple queue implementation in Python:

```python
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue Underflow"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def display(self):
        if not self.is_empty():
            print("Queue elements are:", self.queue)
        else:
            print("Queue is empty")

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(20)
    print("Front of queue:", q.peek())  # Output: 5
    q.dequeue()
    q.display()  # Output: [10, 20]
```

---

## Advantages of Queue

1. **Order Preservation**: Queues maintain the order of elements, ensuring that the first element added is the first to be processed.
2. **Efficient Resource Management**: They are ideal for resource-sharing environments like CPU or printer scheduling.
3. **Concurrency Support**: Queues are fundamental in handling tasks in multithreading environments where multiple producers and consumers exist.

---

## Limitations of Queue

1. **Fixed Size in Static Arrays**: In array-based queue implementations with fixed sizes, the queue has limited capacity, leading to overflow if more elements are enqueued than the size allows.
2. **Not Suitable for Random Access**: Unlike arrays or linked lists, queues don’t allow random access to elements, making them inefficient for retrieving elements other than the front.

---

## Conclusion

Queues are a fundamental data structure used in various applications, particularly when preserving the order of elements is important. By implementing basic operations like enqueue, dequeue, and peek, you can efficiently manage tasks using the FIFO approach.

Feel free to explore the provided code and use this implementation as a base for solving more complex problems involving queues!

---

**Contributors**: bri

**Date**: October 2024

