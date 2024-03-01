import random
import timeit as ti
import matplotlib.pyplot as plt

class Node:
    #constructor initializing node with data
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    #initialize empty linked list
    def __init__(self):
        self.head = None

    #add new node with data to the head
    def add_head(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    #add new node with dta to the tail
    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    #displays linked lists
    def display_sorted(self):
        current = self.head
        print_container = []
        while current is not None:
            print_container.append(current.data)
            current = current.next_node
        print_container.sort()
        print(print_container)

    #fills the lLL with random data 
    def random_inputs(self, length):
        for i in range(length):
            self.add_tail(random.randint(0, 100))
        return self.head.data
    
    #finds the size of the linked list 
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    #perform binary search 
    #used AI (chatgpt) to help with the binary search code
    def binary_search(self, item):
        current = self.head
        data = []
        while current:
            data.append(current.data)
            current = current.next_node

        data.sort()
        low_index = 0
        high_index = len(data) - 1

        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            mid_item = data[mid_index]
            if mid_item == item:
                return mid_index
            if mid_item > item:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
        return None

class IntArray:
    #initialize integer array with list of 0's 
    def __init__(self, length):
        self.array = [0] * length

    #insert item t at index
    def insert(self, index, item):
        self.array[index] = item

    #display
    def display(self):
        print(self.array)

    #insert random numbers 
    def random_inputs(self):
        for i in range(len(self.array)):
            self.array[i] = random.randint(0, 100)
        return self.array[random.randint(0, len(self.array) - 1)]

    #perform binary search on array 
    #used AI (chatgpt) to help with the binary search code
    def binary_search(self, item):
        self.array.sort()
        low_index = 0
        high_index = len(self.array) - 1

        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2
            mid_item = self.array[mid_index]
            if mid_item == item:
                return mid_index
            if mid_item > item:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
        return None

input_sizes = [1000, 2000, 4000, 8000]
ll_time_array = []
a_time_array = []

#print the times 
for size in input_sizes:
    linked_list_instance = LinkedList()
    ll_num_to_search = linked_list_instance.random_inputs(size)
    ll_time = ti.timeit(lambda: linked_list_instance.binary_search(ll_num_to_search), number=1)
    ll_time_array.append(ll_time)
    del linked_list_instance
    print(f"LinkedList Time: {ll_time:.8}")

    array_instance = IntArray(size)
    a_num_to_search = array_instance.random_inputs()
    a_time = ti.timeit(lambda: array_instance.binary_search(a_num_to_search), number=1)
    a_time_array.append(a_time)
    del array_instance
    print(f"Array Time: {a_time:.8}")

    

#plot the graph 
plt.figure(figsize=(20, 10))
plt.plot(input_sizes, ll_time_array, label='LL', color="blue")
plt.plot(input_sizes, a_time_array, label='array', color="red")
plt.xlabel('Size of Input')
plt.ylabel('Time in seconds')
plt.title('Complexity of Binary Search [LL vs array]')
plt.legend()
plt.show()


