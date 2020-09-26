########################################################################################################################
# Find the kth to last element of a singly linked list
########################################################################################################################

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    # noinspection PyMethodMayBeStatic
    def create_linked_list(self, values):
        head = None
        previous = None
        for a in values:
            n = Node(a)
            if previous is None:
                previous = n
                head = n
            else:
                previous.next = n
                previous = n
        return head

    # noinspection PyMethodMayBeStatic
    def print_linked_list(self, head):
        current = head
        print("-----------------------------------------------------------------------------------------------------")
        while current is not None:
            print(current.data, end='\t')
            current = current.next
        print("\n-----------------------------------------------------------------------------------------------------")

    # noinspection PyMethodMayBeStatic
    def kth_last_element(self, head, k):

        current_pointer = head
        forward_pointer = head
        for a in range(0, k, 1):
            if forward_pointer.next is None:
                print("k exceeds number of inputs")
                return head.data
            forward_pointer = forward_pointer.next

        while forward_pointer.next is not None:
            current_pointer = current_pointer.next
            forward_pointer = forward_pointer.next

        return current_pointer.data


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    k = 0
    head = LinkedList().create_linked_list(numbers)
    LinkedList().print_linked_list(head)
    kth_last_element = LinkedList().kth_last_element(head, k)
    print("Element at distance {} from last:".format(k) + str(kth_last_element))
