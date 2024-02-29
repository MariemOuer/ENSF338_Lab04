
#Question 1: Ai Declaration, I used chargbt to help explain some code lines for me from the list.c file
#as it was a very big file and hard to understand.

# When resizing an array (lines 59-69), `list_resize` - function used for resizing:, 
#the new size includes space for the growth of the array that is needed along with additional space. 
#Allowing for future growth while avoiding re-expansion. 
#This strategy is commonly used to balance between memory usage and the performance overhead 
#of resizing. It does so through a growth factor determined by (line 69)
#`new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;`. The growth factor is 1/8. 
#This is a dynamic array implementations because a trade-off between memory 
#usage and  array allocations.

#Ai Declaration - Chatgbt helped me form my answer before as this section 
#of the exercise was very hard to implement and understand.
import sys
import timeit
import matplotlib.pyplot as plt


my_list = []
oldCapacity = sys.getsizeof(my_list)

for i in range(64):
    my_list.append(i)
    newCapacity = sys.getsizeof(my_list)
    if newCapacity != oldCapacity:
        print("Capacity changed from", oldCapacity, "bytes to", newCapacity, "bytes when length is", len(my_list))
        oldCapacity = newCapacity

#  measure time taken to grow array
measureGrowthTime = lambda change_size, repeats: timeit.repeat(
    stmt="arr.append(0)", 
    setup=f"arr = list(range({change_size}))", 
    number=1, 
    repeat=repeats
)

#  parameters
S = 100000  
repeats = 1000

# Measure time to grow from S to S+1
growthTime_from_S_to_Splus1 = measureGrowthTime(S, repeats)

# Measure time to grow from S-1 to S
growthTime_from_Sminus1_to_S = measureGrowthTime(S - 1, repeats)

# Plotting distributions
plt.figure(figsize=(10, 5))
plt.hist(growthTime_from_S_to_Splus1, bins=30, alpha=0.5, label='S to S+1')
plt.hist(growthTime_from_Sminus1_to_S, bins=30, alpha=0.5, label='S-1 to S')
plt.xlabel('Time to grow array (s)')
plt.ylabel('Frequency')
plt.title('Distribution of growth time of array')
plt.legend()
plt.grid(True)
plt.show()
