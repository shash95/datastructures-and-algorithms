########################################################################################################################
# Check if the linked list contains loops
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
    def add_loop_to_linked_list(self, head, position):
        counter = 0
        current = head
        loop_node = None
        while current is not None:
            counter += 1
            if counter == position:
                loop_node = current
                break
            current = current.next

        # if loop position exceeds length of linked list, no loop is added
        if counter != position:
            return head
        last_node = None
        while True:

            if current.next is None:
                last_node = current
                break
            current = current.next

        last_node.next = loop_node

    # noinspection PyMethodMayBeStatic
    def print_linked_list(self, head, limit):
        current = head
        count = 0
        print(
            "-----------------------------------------------------------------------------------------------------")
        while current is not None:
            print(current.data, end='\t')
            current = current.next
            count += 1
            if count == limit:
                break
        print(
            "\n-----------------------------------------------------------------------------------------------------")


    # noinspection PyMethodMayBeStatic
    def check_loops(self, head):
        current = head
        fast_pointer = head
        slow_pointer = head
        while slow_pointer is not None or fast_pointer is not None:
            slow_pointer = slow_pointer.next
            # check if fast pointer is at end of linked list, then return True
            if fast_pointer is None or fast_pointer.next is None:
                return False, None
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True, slow_pointer
        return False, None

    # noinspection PyMethodMayBeStatic
    def get_loop_start(self, head, collision):
        current = head
        while current != collision:
            current = current.next
            collision = collision.next
        return current

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    loop_position = 11
    head = LinkedList().create_linked_list(numbers)
    LinkedList().add_loop_to_linked_list(head, loop_position)
    print("Printing the linked list")
    LinkedList().print_linked_list(head, len(numbers)*3)
    has_loops, collision = LinkedList().check_loops(head)
    print(has_loops)
    if collision:
        loop_start = LinkedList().get_loop_start(head, collision)
        print(loop_start.data)