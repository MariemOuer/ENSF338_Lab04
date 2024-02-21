def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2


# 1. State and justify what is the best, worst and average case complexity for the code in the previous slide [0.2 pts]
'''
Best Case: 
In the best case scenario, every element in the list li is less than or equal to 5. 
In this case, the inner loop is never executed, resulting in a time complexity of O(n), 
where n is the length of the list.

Worst Case: 
The worst case occurs when every element in the list li is greater than 5. 
In this case, both the outer and inner loops are executed for each element in the list. 
The time complexity in this case would be O(n^2), where n is the length of the list.

Average Case: 
The average case complexity depends on the distribution of elements in the list li. 
If we assume a random distribution of elements, the average case complexity would also be O(n^2) 
because on average, half of the elements will be greater than 5.
'''


# 2. Are average, best, and worst case complexity the same? If not, produce a modified version of the code above for which average, best, and worst case complexity are equivalent. [0.2 pts]
'''
No, the average, best, and worst case complexities are not the same. 
To modify the code such that all three complexities become equivalent, we can simply remove the inner loop, 
ensuring that the code's complexity is O(n) regardless of the input.
'''
# Modified Version
def processdata(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2


'''
In this modified version, there is no condition to check if an element is greater than 5, 
and the inner loop always iterates over all elements of the list li. 
As a result, whether the elements are greater than 5 or not, the inner loop executes 
for all elements in the list for each iteration of the outer loop.
Thus, the complexity becomes O(n^2) for all cases.
'''