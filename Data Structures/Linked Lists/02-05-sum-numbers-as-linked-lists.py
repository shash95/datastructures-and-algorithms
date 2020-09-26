########################################################################################################################
# Numbers are represented as linked lists
# E.g. (7 -> 1 -> 6) + (5 -> 9 -> 2)
# Sum is 617 + 295 = 912
# Output linked list: (2 -> 1 -> 9)
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
    def add_extras(self, target_head, head, carry):
        while head.next is not None:
            n = Node(head.data + carry)
            carry = 0
            target_head.next = n
            target_head = target_head.next
            head = n

    # noinspection PyMethodMayBeStatic
    def sum_linked_lists(self, head1, head2):
        carry = 0
        head3 = None
        current = None
        while head1 is not None and head2 is not None:
            sum = head1.data + head2.data + carry
            carry = int(sum/10)
            sum = sum%10
            n = Node(sum)

            if head3 is None:
                head3 = n
                current = head3
            else:
                current.next = n
                current = current.next
            if head1.next is None or head2.next is None:
                break
            head1 = head1.next
            head2 = head2.next

        if head1.next is not None:
            self.add_extras(current, head1, carry)
        if head2.next is not None:
            self.add_extras(current, head2, carry)
        if head1.next is None and head2.next is None and carry!=0:
            n = Node(carry)
            current.next = n
        return head3

if __name__ == '__main__':
    print("Starting...")
    number1 = [1,1,9]
    number2 = [2,2,2]
    head1 = LinkedList().create_linked_list(number1)
    head2 = LinkedList().create_linked_list(number2)
    LinkedList().print_linked_list(head1)
    LinkedList().print_linked_list(head2)
    head3 = LinkedList().sum_linked_lists(head1, head2)
    LinkedList().print_linked_list(head3)
