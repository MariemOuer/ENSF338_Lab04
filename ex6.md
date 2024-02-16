## 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]
Advantages of Arrays:
Constant-time access to elements by index (O(1)).
Efficient memory usage due to contiguous memory allocation.
Cache-friendly, leading to better performance in scenarios where locality of reference matters.
Simple implementation and usage.

Disadvantages of Arrays:
Fixed size, requiring resizing and copying of elements if the array needs to grow beyond its initial capacity.
Costly insertion and deletion operations (O(n)) as elements need to be shifted.

Advantages of Linked Lists:
Dynamic size, allowing for efficient insertion and deletion operations (O(1)) by simply adjusting pointers.
No need for resizing or copying when elements are added or removed.
Flexibility in memory allocation, as nodes can be scattered across memory.

Disadvantages of Linked Lists:
No constant-time access to elements by index; traversal from the beginning or end of the list is required (O(n)).
Higher memory overhead due to the storage of additional pointers for each element.
Less cache-friendly compared to arrays, leading to potentially slower performance in scenarios where locality of reference is important.

## 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? [0.1 pts]
Implementing a replace function in an array to minimize the impact of each standalone task involves the following approach:

Deletion: To minimize the impact of deletion, instead of shifting all elements after the deleted element, we can mark the element as deleted without actually removing it from the array. This can be achieved by setting a flag or marking the element as null.

Insertion: When inserting a new element, we look for the first marked (deleted) element in the array and replace it with the new element. If no marked element is found, we simply append the new element to the end of the array. This ensures that the impact of insertion is minimized since we don't need to shift elements to accommodate the new element.

# Basic Implementation
def replace(arr, index, new_element):
    # Mark the element at the given index as deleted
    arr[index] = None
    
    # Search for the first marked (deleted) element in the array
    for i in range(index + 1, len(arr)):
        if arr[i] is None:
            arr[i] = new_element
            return
    
    # If no marked element is found, append the new element to the end of the array
    arr.append(new_element)


## 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them. [0.4 pts]
# 1. Insertion sort
Feasibility: 
Insertion sort can be implemented for a doubly linked list, but it might not be the most efficient choice. Insertion sort works well for small datasets or nearly sorted lists, as it iterates through the elements, inserting each element into its correct position in the sorted portion of the list. For a doubly linked list, insertion into the correct position can be done efficiently since we have access to both the previous and next elements. However, insertion sort's time complexity is O(n^2) in the worst case, which might not be optimal for larger lists. Additionally, insertion sort's main advantage is its simplicity, but other sorting algorithms like merge sort might provide better performance for larger lists.

Expected Complexity: 
The expected time complexity of insertion sort for a doubly linked list is O(n^2), which is the same as when applied to a regular array. However, insertion sort might perform slightly better on a doubly linked list due to the efficient insertion operation.

# 2. Merge sort
Feasibility: Merge sort is well-suited for sorting doubly linked lists. Merge sort divides the list into smaller sublists, sorts them individually, and then merges them back together. This algorithm works efficiently with linked lists because it only requires changing pointers to rearrange elements, and it doesn't need random access to elements like some other sorting algorithms. Therefore, merge sort can be implemented effectively for a doubly linked list.

Expected Complexity: The expected time complexity of merge sort for a doubly linked list is O(n log n), where n is the number of elements in the list. This complexity is the same as when merge sort is applied to a regular array. However, merge sort might have slightly higher overhead for linked lists due to pointer manipulation, but it remains an efficient choice overall.

In summary, both insertion sort and merge sort can be implemented for a doubly linked list. However, merge sort is generally a better choice due to its superior time complexity and efficient implementation with linked lists. While insertion sort might perform adequately for smaller datasets, its time complexity can be prohibitive for larger lists.


## 4. Also show the expected complexity for each and how it differs from applying it to a regular array [0.4 pts]
Insertion Sort:
Expected Time Complexity for Doubly Linked List: O(n^2)
Expected Time Complexity for Regular Array: O(n^2)
Explanation: In both cases, the time complexity of insertion sort is the same because it involves iterating through the list and inserting each element into its correct position. While insertion sort's time complexity remains O(n^2) for both linked lists and arrays, it might perform slightly better on a doubly linked list due to the efficient insertion operation.

Merge Sort:
Expected Time Complexity for Doubly Linked List: O(n log n)
Expected Time Complexity for Regular Array: O(n log n)
Explanation: Merge sort's time complexity remains O(n log n) for both linked lists and arrays. Merge sort divides the list into smaller sublists, sorts them individually, and then merges them back together. This algorithm works efficiently with linked lists because it only requires changing pointers to rearrange elements, and it doesn't need random access to elements like some other sorting algorithms. Therefore, the time complexity remains the same regardless of whether it's applied to a linked list or an array.
