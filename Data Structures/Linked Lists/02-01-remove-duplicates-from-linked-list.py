########################################################################################################################
# Remove the duplicates from linked list
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
        print(
            "-------------------------------------------------------------------------------------------------------")
        current = head
        while current is not None:
            print(current.data, end='\t')
            current = current.next
        print(
            "\n-------------------------------------------------------------------------------------------------------")

    # noinspection PyMethodMayBeStatic
    def delete_from_linked_list(self, head, value):
        # print(str(head.data) + "\t" + str(value))
        while head.data == value:
            if head.next is None:
                return None
            head = head.next
        current = head
        if current.next is None:
            return current
        forward = current.next
        while forward.next is not None:
            if forward.data == value:
                current.next = forward.next
                forward = current.next
            else:
                current = current.next
                forward = forward.next
        return head

    # noinspection PyMethodMayBeStatic
    def deduplicate_linked_list(self, head):
        current = head
        while current.next is not None:
            new_next = self.delete_from_linked_list(current.next, current.data)
            current.next = new_next
            current = new_next
            # current = current.next
        return head


if __name__ == '__main__':
    print("Starting...")
    numbers = [1,2,1,2,5]
    head = LinkedList().create_linked_list(numbers)
    LinkedList().print_linked_list(head)
    new_head = LinkedList().deduplicate_linked_list(head)
    LinkedList().print_linked_list(new_head)
    print("Done!!!")