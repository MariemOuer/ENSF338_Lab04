
#Question 1: Ai Declaration, I used chargbt to help explain some code lines for me from the list.c file
#as it was a very large file that was hard to understand.

# When resizing an array (lines 59-69), `list_resize` - function used for resizing:, 
#the new size includes space for the growth of the array that is needed along with additional space. 
#Allowing for future growth while avoiding re-expansion. 
#This strategy is commonly used to balance between memory usage and the performance overhead 
#of resizing. It does so through a growth factor determined by (line 69)
#`new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;`. The growth factor is 1/8. 
#This is a dynamic array implementations because a trade-off between memory 
#usage and  array allocations.


#AI generation used for this exercise, Our code was mosty right but there was so much syntax errors that we could not fix
#so we ran it thorugh chatgbt to fix the bugs and make it functional.
import sys
import timeit
import matplotlib.pyplot as plt
maximumSize = 80
experimentRepeats = 1000

def check_list_capacity_changes(maximumSize):
    sampleList = []
    initialCapacity = sys.getsizeof(sampleList)
    for i in range(maximumSize):
        sampleList.append(i)
        currentCapacity = sys.getsizeof(sampleList)
        if currentCapacity != initialCapacity:
            print(f"Capacity changed: Length {len(sampleList)}, Size {currentCapacity} bytes")
            initialCapacity = currentCapacity

def measure_growth(size, repetitions):
    setupCode = f"temp_list = list(range({size}))"
    testCode = "temp_list.append(None)"
    times = timeit.repeat(stmt=testCode, setup=setupCode, number=1, repeat=repetitions)
    return times


# Check list capacity changes AND measures time
check_list_capacity_changes(maximumSize)
growthTime_S_minus_1 = measure_growth(63, experimentRepeats)  
growthTime_S = measure_growth(80, experimentRepeats)          

# Plotting 
plt.figure(figsize=(10, 5))
plt.hist(growthTime_S_minus_1, bins=30, alpha=0.7, label='S-1 to S', color='blue')
plt.hist(growthTime_S, bins=30, alpha=0.7, label='S to S+1', color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Array Growth Time Distribution')
plt.legend()
plt.grid(True)
plt.show()


# Plotting distributions

#The distinction between the two measurements is all about how long it takes 
#to adjust the size of an array. The growth of S to S+1 takes longer than S-1 to S: 

# Array Growth from Size S-1 to S:
# When the array grows from size S-1 to S, it does so within it's current allocated capacity.
# Therefore, there will be no resizing needed. - Adding a new element is faster because it's directly put wihtin the current array.

# Array Growth from Size S to S+1:
# When the array grows from size S to S+1, it usually gets to its current capacity limit.
# Therefore, the process of adding a new element needs to be done after resizing. This process includes allocating a bigger chunk of memory, 
#copying all of the already existing elements, and then adding the new ones.
