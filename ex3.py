
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