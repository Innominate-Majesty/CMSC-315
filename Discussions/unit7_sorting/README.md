# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

--> One of the concepts that I learned while completing this assignment is how Bubble Sort compares neighboring values and swaps them when they are out of order. It continues making passes through the list until no more values need to be swapped. I also learned that Bubble Sort can stop early when a complete pass is made without any swaps. Another concept that I learned is how Merge Sort divides a list into smaller parts and combines them in sorted order. Merge Sort uses recursion to continue dividing the list until each part contains one value. The merge() function then compares and combines those smaller parts to create the final sorted list.


2. What challenges did you encounter, and how did you overcome them?

--> Although it was not a major challenge, I wanted to see how each sorting algorithm worked step by step. To accomplish this, I added a step counter and printed the list after each pass of Bubble Sort. For Merge Sort, I displayed the smaller lists being combined during each step. This made it easier for me to understand how the two algorithms follow different processes to produce the same result. It also helped me find mistakes because I could see exactly when the order of the values changed. After testing both algorithms with several datasets and edge cases, I confirmed that they produced matching results.

3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

--> Bubble Sort is simple to understand because it repeatedly compares neighboring values and swaps them when needed. However, it can become slow with large lists because it might need to make many passes and comparisons. Merge Sort is generally faster for larger datasets because it divides the list into smaller parts before combining them in order. The tradeoff is that Merge Sort is more complex and uses additional memory to create and merge smaller lists. Bubble Sort is a bit of a reasonable choice for small or almost sorted lists, especially because it can stop early when no swaps happened. Merge Sort is a better choice for larger lists when faster and more consistent performance is important.