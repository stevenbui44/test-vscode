import os
import sys
import random
import datetime

def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"

class Person:
    """A simple class to represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

def main():
    """Main function to run the script."""
    print("Starting the script...")

    # Greet someone
    name = "Alice"
    print(greet(name))

    # Create a Person object
    person = Person(name, 30)
    print(person.introduce())

    # Demonstrate some random functionality
    random_number = random.randint(1, 100)
    print(f"Random number: {random_number}")

    # Print the current date and time
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

    print("Script is done.")

# Run main if the script is run directly
if __name__ == "__main__":
    main()