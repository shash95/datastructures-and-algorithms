########################################################################################################################
# Check if the linked list is palindrome
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
    def split_linked_list(self, head, num_elements):
        mid = num_elements/2
        first_half_head = None
        first_half_pointer = None
        second_half_pointer = None
        second_half_head = None
        count = 0
        current = head
        while count < mid:
            n = Node(current.data)
            if first_half_head is None:
                first_half_head = n
                first_half_pointer = first_half_head
            else:
                first_half_pointer.next = n
                first_half_pointer = n
            count += 1
            current = current.next

        while count <= num_elements and current is not None:
            n = Node(current.data)
            if second_half_head is None:
                second_half_head = n
                second_half_pointer = second_half_head
            else:
                second_half_pointer.next = n
                second_half_pointer = n
            count += 1
            current = current.next
        return first_half_head, second_half_head

    # noinspection PyMethodMayBeStatic
    def reverse_linked_list(self, head):

        current = head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

    # noinspection PyMethodMayBeStatic
    def check_palindrome(self, head):
        current = head
        number_of_elements = 0
        while current is not None:
            number_of_elements += 1
            current = current.next

        mid = number_of_elements/2
        first_half_head, second_half_head = self.split_linked_list(head, number_of_elements)
        new_second_half_head = self.reverse_linked_list(second_half_head)

        # iterate over both lists
        first_half_pointer = first_half_head
        second_half_pointer = new_second_half_head
        while first_half_pointer is not None and second_half_pointer is not None:
            if first_half_pointer.data != second_half_pointer.data:
                return False
            first_half_pointer = first_half_pointer.next
            second_half_pointer = second_half_pointer.next

        return True


if __name__ == '__main__':
    text = "radar"
    k = 0
    head = LinkedList().create_linked_list(text)
    LinkedList().print_linked_list(head)
    if LinkedList().check_palindrome(head):
        print("Palindrome linked list")
    else:
        print("Non palindrome linked list")
