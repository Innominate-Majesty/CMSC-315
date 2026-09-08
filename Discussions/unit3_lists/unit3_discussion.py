"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # inserts the value at the specific index
    lst.insert(index, value)

    # items after the inserted value move on position to the right

    # inserting near the front might take longer because there are more items that needs to be moved

    pass


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # checks that the index exists
    if 0 <= index < len(lst):

        # removes and returns the value at the index
        return lst.pop(index)

    # returns none if the index is invalid
    return None

    pass


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # goes through the list item by item
    for index in range(len(lst)):

        # checks if the current item matches the value
        if lst[index] == value:

            # returns the index when value is found
            return index

    # returns -1 if value is not found
    return -1

    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # create a list with several values
    numbers = [10, 20, 30]

    # display the original list
    print("Original list:", numbers)

    # insert a value at the beginning of the list
    insert_at(numbers, 0, 5)
    print("After inserting at the beginning:", numbers)

    # insert a value into the middle of the list
    insert_at(numbers, 2, 15)
    print("After inserting in the middle:", numbers)

    # insert a value at the end of the list
    insert_at(numbers, len(numbers), 40)
    print("After inserting at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # removes the first item from the list
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # remove an item from the middle of the list
    removed = delete_at(numbers, 2)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # remove the last item from the list
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # search for a value that exists in the list
    found_index = search_value(numbers, 20)
    print("Index of 20:", found_index)

    # search for a value that does not exist in the list
    missing_index = search_value(numbers, 100)
    print("Index of 100:", missing_index)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Tries to delete an item using an invalid index.
    invalid_delete = delete_at(numbers, 100)
    print("Delete with invalid index:", invalid_delete)

    # Searches for a value that is not in the list.
    missing_value = search_value(numbers, 999)
    print("Search for missing value:", missing_value)

if __name__ == "__main__":
    main()
