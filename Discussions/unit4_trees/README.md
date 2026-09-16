# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

--> While completing this assignment, I learned how to implement trees in Python. I also learned how recursive methods can be used to insert and search for values in a BST. The in order traversal helped me understand how the left, current, and right nodes are visited to put the values in order.

2. What challenges did you encounter, and how did you overcome them?

--> One of the challenges that I encountered was coming up with the value that would be in the tree. Since it's a tree, I thought fruits would be nice to have in it so I made mine containing fruits. Another challenge was figuring out how the fruit names can be compared. I decided to compare them by the length of their names, which gave each fruit a number that could be used to place it in the tree. Testing the traverdsal and search results helped me make sure the tree was working correctly.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

--> A BST organizes values by comparing them as they are added. Smaller values go to the left, while the larger values go to the right. This ordering makes searching more efficient because each comparison tells the program which side of the tree to check, and the other side can be skipped. In comparison, a regular list might need to check every item one at a time until it finds the correct value. A BST can reduce the amount of searching needs as long as the tree is organized to return the values in order from smallest to largest.