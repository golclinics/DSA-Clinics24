# Stack: Data Structure Overview

A **Stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added to the stack is the first one to be removed. Stacks are widely used in various computer science applications due to their simple yet powerful structure.

## Table of Contents

- [Stack: Data Structure Overview](#stack-data-structure-overview)
  - [Table of Contents](#table-of-contents)
  - [What is a Stack?](#what-is-a-stack)
  - [Operations on a Stack](#operations-on-a-stack)
  - [Applications of Stack](#applications-of-stack)
    - [1. **Function Call Management**](#1-function-call-management)
    - [2. **Undo/Redo Operations**](#2-undoredo-operations)
    - [3. **Expression Evaluation (Postfix/Infix/Prefix)**](#3-expression-evaluation-postfixinfixprefix)
    - [4. **Balanced Parentheses**](#4-balanced-parentheses)
    - [5. **Backtracking Algorithms**](#5-backtracking-algorithms)
  - [Pseudocode and Example Implementation](#pseudocode-and-example-implementation)
  - [Advantages of Stack](#advantages-of-stack)
  - [Limitations of Stack](#limitations-of-stack)
  - [Conclusion](#conclusion)

---

## What is a Stack?

A **Stack** is an abstract data type (ADT) that stores a collection of elements and allows for two main operations: **push** and **pop**. The stack works on the **LIFO (Last In, First Out)** principle, where the last item inserted is the first one to be removed.

Imagine a stack of plates: you can only remove the plate on the top and also add a new plate to the top. This behavior defines the LIFO characteristic of a stack.

---

## Operations on a Stack

A stack typically supports the following fundamental operations:

1. **Push**: Adds an element to the top of the stack.
   - **Pseudocode**:
     ```text
     Push(stack, element):
       if stack is full:
           return "Stack Overflow"
       else:
           increment top
           stack[top] = element
     ```

2. **Pop**: Removes and returns the top element of the stack.
   - **Pseudocode**:
     ```text
     Pop(stack):
       if stack is empty:
           return "Stack Underflow"
       else:
           element = stack[top]
           decrement top
           return element
     ```

3. **Peek (Top)**: Returns the top element without removing it from the stack.
   - **Pseudocode**:
     ```text
     Peek(stack):
       if stack is empty:
           return "Stack is empty"
       else:
           return stack[top]
     ```

4. **IsEmpty**: Checks if the stack is empty.
   - **Pseudocode**:
     ```text
     IsEmpty(stack):
       if top == -1:
           return True
       else:
           return False
     ```

5. **IsFull**: Checks if the stack is full (only relevant in fixed-size implementations).
   - **Pseudocode**:
     ```text
     IsFull(stack):
       if top == max_size - 1:
           return True
       else:
           return False
     ```

---

## Applications of Stack

Stacks are a key data structure in computer science and have various applications:

### 1. **Function Call Management**
   - **Description**: When a function is called, the system places the function's local variables and return address on a call stack. After the function completes, it pops the return address from the stack to resume execution.
   
### 2. **Undo/Redo Operations**
   - **Description**: Text editors, image editors, and similar applications use stacks to maintain a history of actions. Each action is "pushed" onto the stack, and when an undo/redo operation is triggered, actions are "popped" from the stack.

### 3. **Expression Evaluation (Postfix/Infix/Prefix)**
   - **Description**: Stacks are used to evaluate and convert expressions, especially in converting from infix to postfix notation (Reverse Polish Notation) or evaluating postfix expressions.

### 4. **Balanced Parentheses**
   - **Description**: Stacks can be used to check for balanced parentheses in a string (e.g., ensuring that every opening parenthesis has a corresponding closing parenthesis).

### 5. **Backtracking Algorithms**
   - **Description**: Algorithms like depth-first search (DFS) for tree/graph traversal and certain maze solvers utilize stacks to keep track of the nodes or positions visited.

---

## Pseudocode and Example Implementation

Here’s a simple stack implementation in Python:

```python
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def display(self):
        if not self.is_empty():
            print("Stack elements are:", self.stack)
        else:
            print("Stack is empty")

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(20)
    print("Top of stack:", s.peek())  # Output: 20
    s.pop()
    s.display()  # Output: [5, 10]
```

---

## Advantages of Stack

1. **Simple and Easy to Implement**: Stacks have a simple structure and are easy to implement.
2. **Efficient Memory Use**: In most cases, stacks use memory efficiently, especially in recursion and function call handling.
3. **Ideal for Reversing Data**: They provide an easy way to reverse data or store history, which is useful for undo/redo operations.

---

## Limitations of Stack

1. **Fixed Size in Static Arrays**: In static array-based implementations, the stack has a fixed size, leading to stack overflow if more elements are pushed.
2. **Limited Access**: A stack only allows access to the topmost element, making it inefficient for accessing elements in the middle or bottom.
3. **Not Suitable for Sequential Access**: Unlike arrays or linked lists, stacks are not ideal for sequentially traversing elements.

---

## Conclusion

Stacks are a fundamental and versatile data structure, widely used in a variety of applications ranging from managing function calls to undo/redo operations in software. By implementing basic operations like push, pop, and peek, you can efficiently manage data with a LIFO approach.

Feel free to explore the provided code and use this implementation as a base for solving more complex problems involving stacks!

---

**Contributors**: bri  
**Date**: October 2024
