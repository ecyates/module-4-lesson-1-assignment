# Module 4 - Lesson 1 - Python Modules
Author: Elizabeth Yates

In this repository, I will be completing the following assignment:

## 1. Python Modules and Data Handling Assignment

Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling.

### Task 1: Your Mood Today (main_mood.py)

Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered. 

Code Example:  

    # mood_responses.py
    def mood_response(mood):
        # Implement your response logic here

    # main.py
    import mood_responses
    mood = input("How are you feeling today? ")
    print(mood_responses.mood_response(mood))

Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

## 2. Mastering Python Modules and Aliases

Objective: The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases.

### Task 1: Custom Module with Aliases (main_text.py)

Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

Code Example:

    # text_utils.py
    def reverse_string(s):
        # function to reverse a string

    def capitalize_string(s):
        # function to capitalize a string

    # main.py
    # Import text_utils using an alias and utilize its functions

Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, demonstrating an understanding of custom module creation and aliasing.

