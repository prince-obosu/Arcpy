# Escape Room Game

# This program will introduce me to all the areas covered in class (exception handling with try/except blocks
#basic function building and calling,print statements,variables,while loops
# dictionaries,lists,for loops,if/elif statements
# 04/12/2024

#-------CREATIVE VERSION-------

#The game is an "Escape Room Adventure" set in a mysterious house.
#The player finds themselves trapped inside and must navigate through multiple rooms, each containing various items.
#The objective is to find the hidden key in each room to unlock the door and escape.

#Importing time and random functions

import time
import random

try:
    # Function to display menu options and get user input
    def menu(list_items, question):
        # Display the menu options
        for entry in list_items:
            print(1 + list_items.index(entry), ") ", entry)

        try:
            # Get user input and return the index of the chosen item
            return(int(input(question)) - 1)
        except ValueError:
            # Handle the case where the user enters a non-integer value
            print("\nOops! Type a number, please.\n")

    # Defining the list of rooms with their respective items and key locations
    rooms = {
        "Living Room": {"items": ["sofa", "television stand", "center table", "book shelf"],
                        "key_location": 2},
        "Kitchen": {"items": ["sink", "refrigerator", "stove", "cabinets"],
                    "key_location": 1},
        "Bedroom": {"items": ["bed", "dresser","wardrobe", "nightstand"],
                    "key_location": 0}
    }

    # Initialize player's score
    score = 0

    # Display game introduction and instructions
    print("Welcome to the Escape Room Adventure!")
    print("You find yourself trapped in a mysterious house.")
    print("Your objective: Find the hidden key in each room to unlock the door and escape!")
    print("You'll explore multiple rooms, each with its own challenges.")
    print("In each room, you can see various items.")
    print("You must find the key hidden in one of these items to proceed to the next room.")
    print("Be careful! Time is ticking and your score depends on how quickly you escape!\n")

    # Start the timer
    start_time = time.time()

    # Main game loop
    for room_name, room_data in rooms.items():
        print("\n<<<<<<<<<<>>>>>>>>>>>>>>")
        print(f"You are now in the {room_name}. Explore carefully to find the key!\n")

        # Allow the player to explore the room and find the key
        key_found = False
        while not key_found:
            choice = menu(room_data["items"], "What item do you want to investigate? ")
            if choice == room_data["key_location"]:
                print("\n🎉 Congratulations! You found the key and unlocked the door! 💃🕺")
                key_found = True

                # Increase score based on time taken to find the key
                # Shorter time period taken to find the key will have a higher score based on the formular
                elapsed_time = time.time() - start_time
                print(elapsed_time)
                score += int(1000 / elapsed_time)
            else:
                print("\n😔 Sorry, no key here. Keep searching! 😢\n")

    # Calculate the total time taken to escape and display the score
    total_time = time.time() - start_time
    print("\n<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
    print(f"\nYou have successfully escaped the house in {int(total_time)} seconds!")
    print(f"Your final score is: {score}")
    print("Share your victory on social media and challenge your friends to beat your score!")

except:
    # Handle any unexpected errors that may occur during execution
    print("\nUh oh. Something went wrong. Time to check your code.")
