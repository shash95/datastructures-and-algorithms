########################################################################################################################
# Create binary tree and implement all traversals
########################################################################################################################


class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:

    # noinspection PyMethodMayBeStatic
    def create_tree(self):

        node_list = []
        number_of_nodes = 5
        for num in range(0, number_of_nodes, 1):
            node_list.append(Node(num))

        # creating tree
        node_list[0].left = node_list[1]
        node_list[0].right = node_list[2]
        node_list[1].left = node_list[3]
        node_list[2].left = node_list[4]
        return node_list[0]

    # noinspection PyMethodMayBeStatic
    def pre_order(self, root):
        print(root.data)
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)

    # noinspection PyMethodMayBeStatic
    def in_order(self, root):
        if root.left is not None:
            self.in_order(root.left)
        print(root.data)
        if root.right is not None:
            self.in_order(root.right)

    # noinspection PyMethodMayBeStatic
    def post_order(self, root):
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right)
        print(root.data)


if __name__ == '__main__':

    root = Tree().create_tree()
    print("Printing pre order traversal for binary tree")
    Tree().pre_order(root)
    print("Printing in order traversal for binary tree")
    Tree().in_order(root)
    print("Printing post order traversal for binary tree")
    Tree().post_order(root)
