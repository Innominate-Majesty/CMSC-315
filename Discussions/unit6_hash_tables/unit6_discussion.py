"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    ## How a dictionary behaves like a hash table:
    ### A dictionary works like a hash table by using a key to store and find each value
    ### Python converts each key into a hash value to determine where its value is stored
    ### This makes searching for a play's score fast and efficient (doesn't have to be player and score, it can be anything (e.g. SKU and quantity))

    # create an empty dictionary called player scores
    player_scores = {}

    # add player Ayo and Ayo's score to the dictionary
    player_scores["Ayo"] = 1250

    # add player Bao and Bao's score to the dictionary
    player_scores["Bao"] = 980

    # add player Enzo and Enzo's score to the dictionary
    player_scores["Enzo"] = 1420

    # add player Idris and Idris's score to the dictionary
    player_scores["Idris"] = 1100

    # add player Kira and Kira's score to the dictionary
    player_scores["Kira"] = 875

    # add player Noor and Noor's score to the dictionary
    player_scores["Noor"] = 1330

    print("\n=== INSERT OPERATIONS ===")

    # print("TODO: Create a dictionary and add multiple key-value pairs.")

    # display all player names and scores stored in the dictionary
    print("Player scores:", player_scores)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    ## How the lookup works:
    ### A dictionary lookup uses the key's hash value to quickly locate its associated value
    ### In these lookups, the player names are the keys and their scores are the values

    print("\n=== LOOKUP OPERATIONS ===")

    # print("TODO: Demonstrate successful key lookups.")

    # ask user to enter the name of the player that they want to find
    player_name = input("Enter a player's name to look up: ")

    # remove extra spaces and normalize the capitalization of the player's name
    player_name = player_name.strip().title()

    # Look up the player's score and return None if the name is not found
    player_score = player_scores.get(player_name)

    # check if the player's name exists in the dictionary
    if player_score is not None:

        # print the player's name and score when the player is found
        print(player_name + "'s score: ", player_score)
    
    # else: if the player's name doesn't exist in the dictionary
    else:

        # print message: player was not found
        print(player_name, "was not found.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    ## What happens when an existing key is assigned a new value:
    ### When an existing key is assigned a new value, the old value is replaced
    ### The key remains in the dictionary so a duplicate key is not created

    print("\n=== UPDATE OPERATIONS ===")

    # print("TODO: Demonstrate updating an existing key.")

    # print the dictionary before allowing updates
    print("Before update:", player_scores)

    # ask the user to enter the name of the player they want to update
    player_name = input("Enter the player's name to update: ")

    # remove extra spaces and normalize the capitalization of the player's name
    player_name = player_name.strip().title()

    # if the player exists in the dictionary
    if player_name in player_scores:

        # ask the user to enter the player's new score and convert it to an integer
        new_score = int(input("Enter the new score: "))

        # replace the player's existing score with the new score
        player_scores[player_name] = new_score

        # display a message confirming that the score was updated
        print(player_name + "'s score was updated.")

        # print the updated player + scores
        print("After update:", player_scores)

    # else: the player doesn't exist
    else:

        # tell the user that the player could not be found.
        print(player_name, "was not found, so no score was updated.") 

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    ## What happens when a key is removed:
    ### when a key is removed, its associated value is also removed from the dictionary
    ### The deleted key can no longer be used to retrieve that value

    print("\n=== DELETE OPERATIONS ===")

    # print("TODO: Demonstrate deleting a key-value pair.")

    # print dictionary before operating the delete function
    print("Before deletion:", player_scores)

    # ask the user to enter the name of the player they want to update
    player_name = input("Enter the player's name to delete: ")

    # remove extra spaces and normalize the capitalization of the player's name
    player_name = player_name.strip().title()

    # if the player exists in the dictionary
    if player_name in player_scores:

        # remove the player and their score from the dictionary
        del player_scores[player_name]

        # print a message confirming that the player was deleted
        print(player_name, "was deleted.")

        # print the dictionary after the player is deleted
        print("After deletion:", player_scores)

    # else: the player doesn't exist
    else:

        # tell the user that the player could not be found.
        print(player_name, "was not found, so nothing was deleted.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # print("TODO: Demonstrate and explain edge cases.")

    ## Edge case 1: update a missing key 
    ## when a value is assigned to a key that doesn't exist, Python adds the key and value to the dictionary
    ## this means that updating a missing key creates a new key-value pair instead

    # edge case 1: update a missing key
    print("\nEdge Case 1: Update a missing key")

    # print the dictionary before updating the missing key
    print("Before updating missing key:", player_scores)

    # assign a score to Mika even though Mika is not currently in the dictionary
    player_scores["Mika"] = 1050

    # print message explaining that the missing key was added
    print("Mika was not found, so Python added Mika as a new key.")

    # print the dictionary after the missing key was added
    print("After updating missing key:", player_scores)

    ## Edge case 2: Use an empty dictionary
    ## an empty dictionary doesn't contain any keys or values but it's still a valid dictionary
    ## so the program checks whether or not the dictionary is empty before trying to use the data in it

    # create an empty dictionary called empty_player_scores
    empty_player_scores = {}

    # print the empty dictionary
    print("Empty dictionary:", empty_player_scores)

    # check if the dictionary has no key-value pairs
    if not empty_player_scores:

        # print message explaining that the dictionary is empty
        print("The dictionary is empty and does not contain any players or scores.")


if __name__ == "__main__":
    main()