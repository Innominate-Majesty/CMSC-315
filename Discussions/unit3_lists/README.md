# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

--> While completing this assignment, I learned more about creating lists and working with common list operations in Python, such as inserting, deleting, and searching for values. I usually work with these types of operations in Java and occasionally in C and C++ for other courses, so this assignmnet helped me see how the same ideas are handled in Python.

2. What challenges did you encounter, and how did you overcome them?

--> One challenge was coming up with good edge cases to test. It was easy to test the normal cases where the index or value existed but the edge cases required thinking about what could go wrong. For example, using an invalid index or searching for a value that is not in the list. I handled this by adding checks in the code and testing those situations to make sure the program returned None or -1 instead of failing.

3. How do list operations impact performance in real-world applications?

--> List operations can affect performance depending on where the operation happens and how large the list is. Adding or removing items near the beginning or middle can take more time because other items might need to shift positions. Searching can also take longer because the list might need to be checked one item at a time. In terms of real world applications with a lot of data, choosing the right list operation can make a noticeable difference in how quickly the program runs. In any case, I think it is important to weigh the pros and cons of each data structure before choosing one for a specific application or use case.
