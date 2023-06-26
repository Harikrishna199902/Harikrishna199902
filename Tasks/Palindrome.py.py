
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome(head):
    values = []
    current_node = head

    
    while current_node is not None:
        values.append(current_node.value)
        current_node = current_node.next

    
    return values == values[::-1]   


head = Node(1)
head.next = Node(2)
head.next.next = Node(6)
head.next.next.next = Node(2)
head.next.next.next.next = Node(8)

result = is_palindrome(head)
print(result)  # Output: True
