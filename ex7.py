import timeit
import matplotlib.pyplot as plt

class LinkedList:

    #initialize empty linked list 
    def __init__(self):
        self.head = None
    
    #add new node with data to the head
    def insert_head(self, new_node):
        new_node.next_node = self.head
        self.head = new_node

    #add new node with data to the tail
    def insert_tail(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    #find the size 
    def get_size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next_node
        return size
    
    #find the node position
    def get_node_at_position(self, position):
        current_node = self.head
        for _ in range(position):
            if current_node is None:
                return None
            current_node = current_node.next_node
        return current_node
    
    def unoptimized_reverse(self):
        new_head = None
        previous_node = None
        for i in range(self.get_size() - 1, -1, -1):
            current_node = self.get_node_at_position(i)
            new_node = Node(current_node.data)
            if new_head is None:
                new_head = new_node
            else:
                previous_node.next_node = new_node
            previous_node = new_node
        self.head = new_head
    
    def optimized_reverse(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

#create the linked list 
def create_linked_list(size):
    linked_list = LinkedList()
    for i in range(size):
        linked_list.insert_tail(Node(i))
    return linked_list

#calculate the times required
def measure_time(sizes, method_type):
    times = []
    for size in sizes:
        linked_list = create_linked_list(size)
        if method_type == "optimized":
            time = timeit.timeit(lambda: linked_list.optimized_reverse(), number=100)
        elif method_type == "unoptimized":
            time = timeit.timeit(lambda: linked_list.unoptimized_reverse(), number=100)
        times.append(time)
    return times

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

sizes = [1000, 2000, 3000, 4000]
unoptimized_execution_times = measure_time(sizes, "unoptimized")
optimized_execution_times = measure_time(sizes, "optimized")

plt.plot(sizes, unoptimized_execution_times, label="Original Function")
plt.plot(sizes, optimized_execution_times, label="Optimized Function")
plt.xlabel("Size of List")
plt.ylabel("Time Required in seconds")
plt.title("Optimized vs Unoptimized Reverse List")
plt.legend()
plt.show()