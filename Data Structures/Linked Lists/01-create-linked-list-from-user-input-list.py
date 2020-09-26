class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


head = None
previous = None
number_of_inputs = input("Enter number of elements for linked list\n")
for a in range(0,int(number_of_inputs),1):
    user_input = input("Enter value number {}\n".format(str(a+1)))
    n = Node(user_input)
    if previous is None:
        previous = n
        head = n
    else:
        previous.next = n
        previous = n

print("***Accepted all inputs, now generating list***")
print(".\n.\n.\n.")
current = head
while current is not None:
    print(current.data, end='\t')
    current = current.next