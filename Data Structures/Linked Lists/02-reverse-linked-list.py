
class Node:
    value = None
    next = None

    def __init__(self, n):
        self.value = n
        self.next = None


class LinkedList:

    def print_linked_list(self, head):
        while head is not None:
            print(head.value,end='->')
            head = head.next
        # remove last two characters when list is exhausted
        print('\b\b')


    def reverse_linked_list(self, head):
        # if linked list is empty or contains only one value return head
        if head is None or head.next is None:
            return head
        prev = next = None
        curr = head
        while curr is not None:
            # store next value
            next = curr.next
            # reverse link for the current node
            curr.next = prev
            # move prev by one
            prev = curr
            # move curr by one
            curr = next
        return prev


if __name__ == '__main__':

    values = [1,2,3,4]
    head = previous = None
    for value in values:
        current = Node(value)
        if head is None:
            head = current
            previous = current
            continue
        previous.next = current
        previous = current
    LinkedList().print_linked_list(head)
    head = LinkedList().reverse_linked_list(head)
    LinkedList().print_linked_list(head)

