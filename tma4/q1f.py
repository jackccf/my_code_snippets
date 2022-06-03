# tma4 q1f
# purpose: a python program that use binarytee module to build and print some required binary trees 
# written by Cheung Chun Fai (s1285547)
# On 4/24/2021
# For tma4 q1f (comp-s258, 2021Autumn)

from platform import node
from binarytree import Node, build, bst
import random

# CODE HERE for (i)
# use Node class to create nodes in tree with height of 2
cTree = Node(13)
cTree.left = Node(7)
cTree.right = Node(19)
cTree.left.left = Node(5)
cTree.left.right = Node(11)
cTree.right.left = Node(17)
cTree.right.right = Node(23)

print(cTree)

print("Size of tree: ", cTree.size)
print("Height: ", cTree.height)
print("Balanced? ", cTree.is_balanced)
print("Perfect? ", cTree.is_perfect)
print("No of leaves: ", cTree.leaf_count)



# CODE HERE for (ii)
# use bst function to create a random perfect bst with hight of 3
bst_1f2 = bst(height=3, is_perfect=True)
print(bst_1f2)


# CODE HERE for (iii)
print("Size of tree: ", bst_1f2.size)
print("No of leaves: ", bst_1f2.leaf_count)
print(f"The leftmost node is: {bst_1f2.inorder[0]}", sep='', end='')
print(f"The rightmost node is: {bst_1f2.inorder[14]}", sep='', end='')

# help to display result after executing the program
input()
