# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

--> While completing this assignment, I learned how to create and use a hash table in Python. Before this assignment, I did not know that Python dictionaries worked like hash tables. I learned how to add, find, update, and remove information using keys and values. I also learned that each key must be unique so that Python can connect it to the correct value. This activity helped me understand how dictionaries can organize related data.

2. What challenges did you encounter, and how did you overcome them?

--> One challenge I encountered was thinking of useful keys and values for the program. Since the lab already used inventory items with SKUs and quantities, I did not want to repeat the same example in Python. I considered using foods and their prices, but I decided not to use that idea. I eventually chose player names as keys and scores as values. This may not be a perfect example because two players could have the same name, and dictionary keys must be unique. However, it still helped me understand how keys and values work together.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

--> A hash table stores information as key-value pairs, such as a player’s name and score. It uses the key to quickly find the location of its related value. A collision happens when two different keys are assigned to the same storage location. When this occurs, the hash table must use a method to keep the values separate and find the correct one later. Hash tables can improve efficiency because they usually find, add, or remove information without checking every item. This makes them useful when a program needs to work with a large amount of data.