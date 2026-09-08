"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

## name: Venus

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        self.items = []

        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        ## add value to the top of the stack
        self.items.append(value)


        ## Explanation:
        ## LIFO is last in first out, which means that the last item that is added to the stack is going to be the first one to get out
        ## The line above is adding new values at the end, which is the top of the stack

        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        ## check if stack is empty
        if self.is_empty():
            return None
        
        ## pop and return the value at the top of the stack
        return self.items.pop()
    
        ## if the stack is empty, there isn't any value to remove (aka pop)
        ## returning None prevents an error from trying to pop from an empty list

        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        ## check if stack is empty
        if self.is_empty():
            return None
        
        ## return the value that's at the top of the stack 
        return self.items[-1]
    
        ## peek lets you see the most recently added item without changing the stack

        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0
    
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        ## create an empty deque 
        self.items = deque()

        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        ## add new value to the back of the queue
        self.items.append(value)

        ## Explanation:
        ## FIFO is first in first out, which means that the first item that goes into the list will be the first to get out
        ## append adds an item. so in the line above, the new item/value is added at the end of the list (which is self.items)
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        ## check if the queue is empty
        if self.is_empty():

            ## if the queue is empty, then there's no value to remove
            ## returning None prevents an error when trying to dequeue an empty list
            return None
        
        ## remove and return the value at the front of the queue
        return self.items.popleft()
    
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        ## check if the queue is empty 
        if self.is_empty():
            
            ## return none is it's empty
            return None
        
        ## return the value at the front of the queue
        return self.items[0]
    
        ## Explanation:
        ## front is peek but for Queue. It lets the program look at the front/first item in the queue
        ## without changing the queue/list

        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        ## empty = zero items inside
        return len(self.items) == 0
    
        pass


def main():

    print("=== UNIT 2: STACKS AND QUEUES ===")

    ## Picking between stack and queue demos

    ## keep displaying the main menu 

    while True:
        print("\nStack or Queue Demo")

        print("1. Stack")
        print("2. Queue")
        print("3. Quit")

        # Get the user's menu choice.
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            run_stack_demo()

        elif choice == "2":
            run_queue_demo()

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose an option from 1 through 3.")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    def run_stack_demo():
        ## create a new empty stack
        stack = Stack()

        print("\n=== STACK ====")

        ## keep displaying the menu until quit

        while True:

            print("\nCurrent stack:", stack.items)

            print("\nChoose an option:")
            print("1. ADD a value")
            print("2. POP the top value")
            print("3. PEEK the top value")
            print("4. Check if the stack is empty")
            print("5. Clear the stack")
            print("6. Quit")

            # get the user's menu choice
            choice = input("\nEnter your choice: ").strip()


            if choice == "1":
                # Ask the user which value should be added.
                value = input("Enter a value to add: ")

                # Add the value to the top of the stack.
                stack.push(value)

                print(f"Added '{value}' to the top of the stack.")

            elif choice == "2":
                # Remove the most recently added value.
                removed_value = stack.pop()

                # Check whether there was a value available to remove.
                if removed_value is None:
                    print("The stack is empty. There is nothing to pop.")
                else:
                    print(f"Popped '{removed_value}' from the stack.")
                    print("This demonstrates LIFO because the most recently added value was removed first.")

            elif choice == "3":
                # View the top value without removing it.
                top_value = stack.peek()

                # Check whether the stack contains a value to view.
                if top_value is None:
                    print("The stack is empty. There is no value to peek at.")
                else:
                    print(f"The value at the top of the stack is '{top_value}'.")
                    print("The value was not removed.")

            elif choice == "4":
                # Check whether the stack contains any values.
                if stack.is_empty():
                    print("The stack is empty.")
                else:
                    print("The stack is not empty.")

            elif choice == "5":
                # Replace the current stack contents with an empty list.
                stack.items.clear()

                print("The stack has been cleared.")

            elif choice == "6":
                print("Exiting the Stack Demo.")
                print("The stack exists only during this program session.")
                break

            else:
                print("Invalid choice. Please choose an option from 1 through 6.")



    ## print("\n=== STACK DEMO ===")
    ## print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    ## print("      test popping from an empty stack,")
    ## print("      test peeking at an empty stack,")
    ## print("      and verify a single-item stack becomes empty after removal.")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    ## print("\n=== QUEUE DEMO ===")
    ## print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    ## print("      test dequeuing from an empty queue,")
    ## print("      test viewing the front of an empty queue,")
    ## print("      and verify a single-item queue becomes empty after removal.")

    def run_queue_demo():

        ## create a new empty queue
        queue = Queue()

        print("\n=== QUEUE ===")

        ## keep displaying the menu until quit

        while True:

            print("\nCurrent queue:", list(queue.items))

            print("\nChoose an option:")
            print("1. Add a value")
            print("2. Dequeue the front value")
            print("3. View the front value")
            print("4. Check if the queue is empty")
            print("5. Clear the queue")
            print("6. Quit")

            ## get user's menu choice
            choice = input("\nEnter your choice: ").strip()

            # Check whether the user entered the add(value) command.
            if choice.lower().startswith("add(") and choice.endswith(")"):
                # Get the value written between the parentheses.
                value = choice[4:-1]

                # Add the value to the back of the queue.
                queue.enqueue(value)

                print(f"Added '{value}' to the back of the queue.")
                continue

            if choice == "1":
                # Ask the user which value should be added.
                value = input("Enter a value to add: ")

                # Add the value to the back of the queue.
                queue.enqueue(value)

                print(f"Added '{value}' to the back of the queue.")

            elif choice == "2":
                # Remove the value at the front of the queue.
                removed_value = queue.dequeue()

                # Check whether there was a value available to remove.
                if removed_value is None:
                    print("The queue is empty. There is nothing to dequeue.")
                else:
                    print(f"Dequeued '{removed_value}' from the front of the queue.")
                    print(
                        "This demonstrates FIFO because the earliest added "
                        "value was removed first."
                    )

            elif choice == "3":
                # View the front value without removing it.
                front_value = queue.front()

                # Check whether the queue contains a value to view.
                if front_value is None:
                    print("The queue is empty. There is no front value.")
                else:
                    print(f"The value at the front of the queue is '{front_value}'.")
                    print("The value was not removed.")

            elif choice == "4":
                # Check whether the queue contains any values.
                if queue.is_empty():
                    print("The queue is empty.")
                else:
                    print("The queue is not empty.")

            elif choice == "5":
                # Remove all values from the queue.
                queue.items.clear()

                print("The queue has been cleared.")

            elif choice == "6":
                print("Exiting the Queue Demo.")
                print("The queue exists only during this program session.")
                break

            else:
                print("Invalid choice. Please choose an option from 1 through 6.")        

if __name__ == "__main__":
    main()
