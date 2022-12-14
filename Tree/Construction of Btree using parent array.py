class Node:
    	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Function to perform inorder traversal on the tree
def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


# Function to build a binary tree from the given parent list
def createTree(parent):

	# create an empty dictionary
	d = {}

	# create `n` new tree nodes, each having a value from 0 to `n-1`,
	# and store them in a dictionary
	for i in range(len(parent)):
		d[i] = Node(i)

	# represents the root node of a binary tree
	root = None

	# traverse the parent list and build the tree
	for i, e in enumerate(parent):

		# if the parent is -1, set the root to the current node having the
		# value `i` (stored in map[i])
		if e == -1:
			root = d[i]
		else:
			# get the parent for the current node
			ptr = d[e]

			# if the parent's left child is filled, map the node to its right child
			if ptr.left:
				ptr.right = d[i]
			# if the parent's left child is empty, map the node to it
			else:
				ptr.left = d[i]

	# return root of the constructed tree
	return root


if __name__ == '__main__':

	parent = [2,0,-1]

	root = createTree(parent)
	inorder(root)