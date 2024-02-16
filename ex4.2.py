# 3. Provide the code for an inefficient implementation and an efficient implementation. [0.2 pts]
# Inefficient Implementation (Linear Search)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Efficient Implementation (Binary Search)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



# 4. State the worst-case complexity of each. [0.2 pts]
'''
Linear Search: 
O(n), where n is the number of elements in the array. 
This occurs when the target element is either the last element in the array or not present in the array.

Binary Search: 
O(log n), where n is the number of elements in the array. 
This occurs because at each step, the search space is halved.
'''


# 5. Provide the code for an experiment that demonstrates the difference. [0.2 pts] The experiment should:
    # 1. Time the execution of both implementations on realistic, large inputs (1000 elements or above)
    # 2. Plot the distribution of measured values across multiple measurements (>= 100 measurements per task)
import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def time_search(search_func, arr, target, num_measurements):
    measurements = []
    for _ in range(num_measurements):
        start_time = time.time()
        search_func(arr, target)
        end_time = time.time()
        measurements.append(end_time - start_time)
    return measurements

if __name__ == "__main__":
    arr = sorted(random.sample(range(10000), 1000))  # Generating a sorted array of 1000 random elements
    target = random.choice(arr)  # Choosing a random element from the array as the target

    num_measurements = 100
    linear_measurements = time_search(linear_search, arr, target, num_measurements)
    binary_measurements = time_search(binary_search, arr, target, num_measurements)

    plt.hist(linear_measurements, bins=20, alpha=0.5, label='Linear Search')
    plt.hist(binary_measurements, bins=20, alpha=0.5, label='Binary Search')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Execution Time Distribution')
    plt.legend()
    plt.show()

