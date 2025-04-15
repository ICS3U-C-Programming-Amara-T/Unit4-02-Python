#!/usr/bin/env python3

# Created By: Amara Tie

# Date: April 8, 2025

# This is a program gets the sum of a number


def main():

    # Ask User for a number
    user_as_string = input("Enter a positive number :")
    print("")

    # Initialize counter
    loop_counter = 0
    factorial_answer = 1

    # Calculate the factorial of a number
    try:
        user_as_number = int(user_as_string)
        # Check if the number is positive
        if user_as_number >= 0:
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times of loop.".format(loop_counter))
                print("{}! = {}".format(user_as_number, factorial_answer))
                if loop_counter >= user_as_number:
                    break
        else:
            print("Please enter a positive number")
    except Exception:
        print("This is not a number")

if __name__ == "__main__":
    main()
