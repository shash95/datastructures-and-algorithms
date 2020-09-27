########################################################################################################################
# Create minimum height BST from an ascending array
########################################################################################################################
import math
import sys

class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def create_binary_search_tree(self, number_list):

        # if length is 1, only root has to be created
        if len(number_list) == 1:
            new_node = Node(number_list[0])
            return new_node

        # if length is 2, create a child and parent node
        if len(number_list) == 2:
            larger_node = Node(number_list[1])
            smaller_node = Node(number_list[0])
            larger_node.left = smaller_node
            return larger_node

        # if length is greater than 2, split the list into two parts and call the method recursively
        mid_point = math.floor(len(number_list)/2)
        left_head = self.create_binary_search_tree(number_list[0:mid_point])
        right_head = self.create_binary_search_tree(number_list[mid_point+1:])
        # create node from mid point and assign left and right subtrees
        new_node = Node(number_list[mid_point])
        new_node.left = left_head
        new_node.right = right_head
        return new_node

    # noinspection PyMethodMayBeStatic
    def pre_order(self, root):
        print(root.data, end='\t')
        if root.left is not None:
            self.pre_order(root.left)
        if root.right is not None:
            self.pre_order(root.right)

    def validate_bst(self, root, min, max):
        if root is None:
            return True
        left_is_valid = self.validate_bst(root.left, min, root.data)
        right_is_valid = self.validate_bst(root.right, root.data, max)
        if left_is_valid and right_is_valid and root.data > min and root.data < max:
            return True
        return False

if __name__ == '__main__':
    number_list = [1,2,3,4,5,6,7]
    root = BinarySearchTree().create_binary_search_tree(number_list)
    BinarySearchTree().pre_order(root)
    print("")
    print(BinarySearchTree().validate_bst(root, -1*sys.maxsize, sys.maxsize))