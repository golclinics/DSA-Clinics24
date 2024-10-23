import heapq


def priority_queue(tasks):
    output = []

    tasks = [(p, n) for n, p in tasks] # swap order of task name and priority
    heapq.heapify(tasks) # create a min-heap
    
    while tasks:
        output.append(heapq.heappop(tasks)[1])
    
    return output

if __name__ == "__main__":
    output = priority_queue([("task1", 2), ("task2", 1), ("task3", 3)])
    print(*output, sep=" ")
