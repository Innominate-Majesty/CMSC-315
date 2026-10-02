"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # create a copy of the original list so the original list is not changed
    sorted_list = lst.copy()

    # count the sorting steps
    step_number = 1

    # for loop: go through each item in the list
    for pass_number in range(len(sorted_list) - 1):

        # keep track of whether a swap happened or not
        swapped = False

        # for loop: compare each pair of neighboring values that has not been sorted yet
        for index in range(len(sorted_list) - 1 - pass_number):

            # if the value on the left is greater than the value on the right
            if sorted_list[index] > sorted_list[index + 1]:

                # swap the two values so the smaller value is before the larger value
                sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]

                # swapped is now true
                swapped = True
        
        # print the current bubble sort step
        print("Step ", step_number, "is complete.")

        # print the list after the current step
        print("The list is now: ", sorted_list)

        # increase the step number for the next pass
        step_number += 1

        # if no swap happened
        if not swapped:

            # break
            break

    # return the new sorted list
    return sorted_list


def merge_sort(lst, step_counter=None):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # create a shared step counter when merge sort first starts
    if step_counter is None:

        # store the step number in a list so all recursive calls can update it
        step_counter = [1]

    # if the list has one item or is empty
    if len(lst) <= 1:

        # return a copy of the list because the list is already sorted
        return lst.copy()
    
    # find the middle position of the list
    middle = len(lst) // 2

    # create a list with the left half of the original list
    left_half = lst[:middle]

    # create a list with the right half of the original list
    right_half = lst[middle:]

    # use recursion to sort the left half
    sorted_left = merge_sort(left_half, step_counter)

    # use recursion to sort the right half
    sorted_right = merge_sort(right_half, step_counter)

    # combine the two sorted halves
    merged_list = merge(sorted_left, sorted_right)

    # print the current Merge Sort step
    print("Step ", step_counter[0], "is complete.")

    # print the two lists that were combined during this step
    print("Merged ", sorted_left, "and ", sorted_right)

    # print the list that was created during this step
    print("The list is now: ", merged_list)

    # increase the step number for the next merge
    step_counter[0] += 1

    # combine the left and the right halves into a complete list 
    return merged_list

def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    
    # create an empty list for the sorted values
    merged_list = []

    # start at the first index in the left list
    left_index = 0

    # start at the first index in the right list
    right_index = 0

    # while both lists still have values to compare
    while left_index < len(left) and right_index < len(right):

        # if the current value from the left list is smaller or equal
        if left[left_index] <= right[right_index]:

            # add the current value from the left list to the merged list
            merged_list.append(left[left_index])

            # move to the next value in the left list
            left_index += 1

        # else: the current value in the right list is smaller
        else:

            # add the current value from the right list to the merged list
            merged_list.append(right[right_index])

            # move to the next value in the right list
            right_index += 1
    
    # add any values that remain in the left list
    merged_list.extend(left[left_index:])

    # add any values that remain in the right list
    merged_list.extend(right[right_index:])

    # return the completed sorted list
    return merged_list

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # create the first unsorted list
    dataset_1 = [12, 7, 25, 3, 18, 9, 31, 14, 6, 20]

    # print the original unsorted list
    print("Unsorted list: ", dataset_1)

    # print starting bubble sort message
    print("\nStarting Bubble Sort....")

    # sort the first dataset by using bubble sort
    bubble_dataset_1 = bubble_sort(dataset_1)

    # print the sorted list by using bubble sort
    print("Bubble Sort result: ", bubble_dataset_1)

    # print starting merge sort message
    print("\nStarting Merge Sort....")

    # sort dataset 1 using Merge Sort
    merge_dataset_1 = merge_sort(dataset_1)

    # print the sorted list by using merge sort
    print("Merge Sort result: ", merge_dataset_1)

    # compare and print the results from both sorting algorithms
    print("Both results are equal: ", bubble_dataset_1 == merge_dataset_1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    
    # print("TODO: Create a second dataset and compare sorting results.")

    # create the second unsorted list
    dataset_2 = [42, 15, 8, 27, 33, 4, 19, 11, 36, 23]

    # print the original unsorted list
    print("Unsorted list: ", dataset_2)

    # print starting bubble sort message
    print("\nStarting Bubble Sort....")

    # sort the first dataset by using bubble sort
    bubble_dataset_2 = bubble_sort(dataset_2)

    # print the sorted list by using bubble sort
    print("Bubble Sort result: ", bubble_dataset_2)

    # print starting merge sort message
    print("\nStarting Merge Sort....")

    # sort dataset 1 using Merge Sort
    merge_dataset_2 = merge_sort(dataset_2)

    # print the sorted list by using merge sort
    print("Merge Sort result: ", merge_dataset_2)

    # compare and print the results from both sorting algorithms
    print("Both results are equal: ", bubble_dataset_2 == merge_dataset_2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: sorting an empty list
    # since it's empty, it's already sorted
    empty_list = []

    # Edge case 2: sorting an already sorted list
    # the values should remain in the same order
    sorted_list = [3, 8 ,14, 19, 26, 32]

    # Edge case 3: sorting a reverse sorted list
    # the algorithms must completely reverse the order of the values
    reverse_list = [45, 37, 29, 21, 13, 5]

    # Edge case 4: sorting a list with duplicate values
    # the duplicate values should remain in the list after sorting
    duplicate_list = [16, 7, 16, 3, 7, 11, 2, 30]

    # Edge case 5: sorting a single value list
    # since there's only one value in there, it's already sorted
    single_value_list = [64]

    # Edge case 6: sorting an odd length list
    # Merge Sort has to divide this list into two halves with different sizes
    odd_length_list = [17, 4, 29, 8, 13, 2, 21]

    # Edge case 7: sorting negative numbers and zero
    # negative numbers and zero can be compared with positive numbers
    negative_list = [-8, 12, 0, -3, 7, -15, 4]

    # Edge case 8: sorting decimal values
    # decimal values can be sorted in the same way as integers
    decimal_list = [4.5, 1.2, 8.7, 3.3, 0.5]

    # Edge case 9: sorting values with a large range
    # the algorithms compare the values even when their sizes are very different
    large_range_list = [1000000, 2, 50000, -1000000, 75]

    # all edge cases into one list
    edge_cases = [

            # add edge case 1 and its empty dataset
            ("Edge Case 1: Sorting an empty list", empty_list),

            # add edge case 2 and its already sorted dataset
            ("Edge Case 2: Sorting an already sorted list", sorted_list),

            # add edge case 3 and its reverse-sorted dataset
            ("Edge Case 3: Sorting a reverse-sorted list", reverse_list),

            # add edge case 4 and its dataset containing duplicate values
            ("Edge Case 4: Sorting a list with duplicate values", duplicate_list),

            # add edge case 5 and its single-value dataset
            ("Edge Case 5: Sorting a single-value list", single_value_list),

            # add edge case 6 and its odd-length dataset
            ("Edge Case 6: Sorting an odd-length list", odd_length_list),

            # add edge case 7 and its dataset containing negative numbers and zero
            ("Edge Case 7: Sorting negative numbers and zero", negative_list),

            # add edge case 8 and its decimal dataset
            ("Edge Case 8: Sorting decimal values", decimal_list),

            # add edge case 9 and its dataset containing a large range of values
            ("Edge Case 9: Sorting values with a large range", large_range_list)
        ]
    
    # Bubble Sort and Merge Sort all edge cases
    for case_name, dataset in edge_cases:

        # display the numbered name of the current edge case
        print("\n" + case_name)

        # display the original edge-case dataset
        print("Original list:", dataset)

        # tell the user that Bubble Sort is starting
        print("\nStarting Bubble Sort....")

        # sort the current dataset by using Bubble Sort
        bubble_result = bubble_sort(dataset)

        # display the completed Bubble Sort result
        print("Bubble Sort result:", bubble_result)

        # tell the user that Merge Sort is starting
        print("\nStarting Merge Sort....")

        # sort the current dataset by using Merge Sort
        merge_result = merge_sort(dataset)

        # display the completed Merge Sort result
        print("Merge Sort result:", merge_result)

        # compare and display the results from both sorting algorithms
        print("Both results are equal:", bubble_result == merge_result)   


if __name__ == "__main__":
    main()