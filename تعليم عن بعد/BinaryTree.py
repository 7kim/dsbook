class Node:                 # A Node is being created every single time a new part of tree is added.

    def __init__(self, data):                 #the constructor takes one element which is the data or "what the node actually contains"

        self.left = None                  #what is on the left side of the node?
        self.right = None                 #what is on the right side of the node?
        self.data = data                  #what does the node actually contain?

    def insert(self, data):                 #method which inserts a node and relates it to an existing node if available.
# Compare the new value with the parent node
        if self.data:                 #in case self.data exists or != None
            if data < self.data:                 #if the data provided is less than self.data of the existing node
                if self.left is None:                 #if the left side is pointing to None
                    self.left = Node(data)                 #then insert the new node on the left side of the existing parent.
                else:
                    # else means that if the left side of the parent node is not empty ("has someting"), then re-implement the method
                    # of insert on it and start all over again for the new left node applying insert on it.
                    self.left.insert(data)


            elif data > self.data:                 # in case the data provided is greater than self.data of existing node
                if self.right is None:                 # if the right side of the node is pointing to none.
                    self.right = Node(data)                 #create a node with (data), and keep it as self.right of the existing node.
                else:
                    # else means that if the right side of the parent node is not empty ("has someting"), then re-implement the method
                    # of insert on it and start all over again for the new left node applying insert on it.
                    self.right.insert(data)
        else:                 # else means if the self.data doesnt exist, which means that the node is empty.
            self.data = data

# Print the tree
    def PrintTree(self):                 # method to print from in-depth left, print left,middle,right,then go to parent and retry.
        if self.left:                 # if the parent has a node connected to it from the left side
            self.left.PrintTree()                 # implement the method print tree on the left of the parent.
            # this means that the method will keep on looping untill it goes to left end of the graph going in depth through "lefts" of nodes.
        print( self.data),                 # print the self.data of the node which this method is running on.
        if self.right:                 # if the node on left end, has a connected node on right.
            self.right.PrintTree()                 # implement the method print tree on the right of the parent.

# Use the insert method to add nodes
root = Node(5)                     # Parent node contains 12 as self.data and has none on both sides.
root.insert(10)                     # insert 6 into the tree.
root.insert(1)                     # insert 14 into the tree.
root.insert(0)                     # insert 3 into the tree.
root.PrintTree()                     # print me the whole tree, sorting from lowest to highest.
