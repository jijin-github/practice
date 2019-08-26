# Python3 implementation of the approach

# Represents node of the linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Insertion in linked list
def insert(head, item):
    ptr = head
    temp = Node(item)

    if head == None:
        head = temp
    else:
        while ptr.next != None:
            ptr = ptr.next

        ptr.next = temp

    return head


# Function to find the sum of
# non duplicate nodes
def sumOfNonDupNode(head):
    ptr1 = head
    Sum = flag = 0

    while ptr1 != None:
        ptr2, flag = head, False

        # Check if current node
        # has some duplicate
        while ptr2 != None:

            # Check for duplicate node
            if (ptr1 != ptr2 and
                    ptr1.data == ptr2.data):
                flag = True
                break

            # Get to the next node
            ptr2 = ptr2.next

        # If current node is unique
        if not flag:
            Sum += ptr1.data

        # Get to the next node
        ptr1 = ptr1.next

    return Sum


# Driver code
if __name__ == "__main__":
    head = None

    head = insert(head, 1)
    head = insert(head, 2)
    head = insert(head, 1)
    head = insert(head, 3)
    head = insert(head, 4)
    head = insert(head, 3)

    print(sumOfNonDupNode(head))

# This code is contributed by Rituraj Jain
