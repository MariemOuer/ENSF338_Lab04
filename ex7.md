question 1:

    Time complexity: O(n^2)

    Why: 
        get_element_at_pos complexity = O(n) but it has this element by itself it is responsible for a few other jobs that call this function such as node creation, node copying, and repating this which gives a linear time complexity multiplied an unknown number of times (i iterations) which makes it an overall linear increase


OPTIMIZED FUNCTION:

** AI declaration - used AI (chatgpt) to help optimize the code because i was running errors when i did it so put it into AI and it helped fix up my errors **

def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    self.head = prev_node

Changes made:
    I removed the redundant code for the initalization of newhead and prevhead and whiile attempting to reverse the link by changing the next pointers I ran into some errors and used AI to fix the small errors in my code. I also reduced the number of iterations

