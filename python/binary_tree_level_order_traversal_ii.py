# coding=utf-8
# AC Rate: 31.4%
# https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Given a binary tree, return the bottom-up level order traversal of its nodes'
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#'
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        