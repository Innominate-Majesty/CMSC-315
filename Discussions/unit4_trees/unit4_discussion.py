"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None

        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # empty BST doesn't have a root node
        self.root = None

        pass

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # values smaller than a node go to the left while the larger ones go to the right
        self.root = self._insert_recursive(self.root, value)

        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # an empty position is where the new node belongs
        if node is None:
            return Node(value)

        if len(value) < len(node.value):
            node.left = self._insert_recursive(node.left, value)
        
        elif len(value) > len(node.value):
            node.right = self._insert_recursive(node.right, value)

        # return the current node
        return node
    
        pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        return self._search_recursive(self.root, value)
    
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # reaching an empty position means that the value is not in the tree
        if node is None:
            return False

        # the value is found
        if value == node.value:
            return True

        # search only the subtree where the value could exist
        if len(value) < len(node.value):
            return self._search_recursive(node.left, value)
        
        return self._search_recursive(node.right, value)
    
        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values
    
        pass

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # stop when an empty child position is reached
        if node is None:
            return
        
        # visit the left subtree
        # then the current node
        # then the right subtree
        
        # this traversal produces sorted output in a BST because the smaller values are stored on the left and the larger values are on the right

        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)

        pass


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    ## 5. A BST is efficient at reducing search space for each step because each comparison tells which side could have the fruit (or length, value, etc)
    ## shorter names are on the left and longer names are on the right (smaller values --> left && larger values --> right)
    ## this means that you can skip checking one side of the tree if you know that the value you're searching for is smaller or larger

    ## idea: tree with fruits. the fruit's name length is comparison value

    print("\n=== TREE CONSTRUCTION ===")

    # an empty tree to put fruits in
    fruit_tree = BST()

    # fruits in the tree
    # banana = 6
    # apple = 5
    # watermelon = 10
    # fig = 3
    # avocado = 7
    # kiwi = 4
    # blueberry = 9

    fruits = ["banana", "apple", "watermelon", "fig", "avocado", "kiwi", "blueberry"]

    # goes through the fruit list
    for fruit in fruits:

        # adds the current fruit to the tree
        fruit_tree.insert(fruit)

    # print the fruit that was added
    print("Fruits inserted:", fruits)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    ## 3. the traversal produces sorted output in a BST because the values are already organized by length when inserted
    ## the traversal checks the shorter names on the left, the current name, and then the longer names on the right
    ## this puts the fruits in order from shorter to longest name length

    print("\n=== IN-ORDER TRAVERSAL ===")

    # gets the fruits from the tree in order by name length
    fruits_in_order = fruit_tree.inorder()

    # prints the ordered fruit list
    print("Fruits in order:", fruits_in_order)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # searches for four fruits that are in the tree
    print("Is fig in the tree?", fruit_tree.search("fig"))
    print("Is blueberry in the tree?", fruit_tree.search("blueberry"))
    print("Is apple in the tree?", fruit_tree.search("apple"))
    print("Is watermelon in the tree?", fruit_tree.search("watermelon"))

    # searches for four fruits that are not in the tree
    print("Is pear in the tree?", fruit_tree.search("pear"))
    print("Is pineapple in the tree?", fruit_tree.search("pineapple"))
    print("Is orange in the tree?", fruit_tree.search("orange"))
    print("Is strawberry in the tree?", fruit_tree.search("strawberry"))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # makes an empty tree for the first two tests
    empty_tree = BST()

    # test 1: traverses an empty tree
    # since the tree is empty, the traversal reaches an empty node immediately and stops
    print("Empty tree traversal:", empty_tree.inorder())

    # test 2: searches an empty tree
    # this returns false because the tree doesn't have any fruits in it
    print("Search empty tree for apple:", empty_tree.search("apple"))

    # makes a tree with only one fruit
    single_tree = BST()
    single_tree.insert("mango")

    # test 3: traverses a tree with one fruit
    # there's no left or right child nodes to visit because this tree only has 1 fruit
    # the traversal returns only "mango"
    print("Single fruit traversal:", single_tree.inorder())

    # test 4: searches a tree with one fruit
    # "mango" matches the root node so it returns true. the search finds it immediately since it's the only fruit
    print("Search single tree for mango:", single_tree.search("mango"))

    # makes a tree and tries to add the same fruit twice
    duplicate_tree = BST()
    duplicate_tree.insert("banana")
    duplicate_tree.insert("banana")

    # test 5: checks what happens with a duplicate fruit
    # the tree would only contain 1 banana because equal values isn't smaller or larger than one another
    # it can't insert left or right 
    # the second insertion is ignored
    print("Duplicate fruit traversal:", duplicate_tree.inorder())

    # makes a tree with two different fruits that have the same name length
    same_length_tree = BST()
    same_length_tree.insert("apple")
    same_length_tree.insert("mango")

    # test 6: checks what happens when two fruit names have the same length
    # because this tree and program is comparing the fruits based on the length of their names, only apple is inserted and mango will be ignored
    # the second name with the same length as the first one is treated as if it's a duplicate
    print("Same length traversal:", same_length_tree.inorder())


if __name__ == "__main__":
    main()
