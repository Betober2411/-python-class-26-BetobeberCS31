# Module file for Lab 5  - nameformat.py

"""
nameformat - Name formatting module for Lab 5.

Provides small helper functions that greet a user and display
their name in different formats.
"""

def hello_world():
    """Print a simple seasonal greeting."""
    print("Hello Halloween 2026!")


def sayHello(firstName):
    """Say hello to the given first name."""
    print(f"Hello there {firstName}. Mighty fine day we're having!")
    print()


def fullName(firstName, lastName):
    """Output the full name in the format: First Last."""
    print(f"{firstName} {lastName}")
    print()


def lastNameFirst(firstName, lastName):
    """Output the name with the last name first, separated by a comma:
    Last, First."""
    print(f"{lastName}, {firstName}")
    print()

def documentation():
    """Display the documentation for this module and its functions."""
    print("=" * 50)
    print("MODULE DOCUMENTATION")
    print("=" * 50)
    print(__doc__.strip())
    print()

    print("Functions:")
    print(f"  sayHello(firstName)\n      {sayHello.__doc__}")
    print(f"  fullName(firstName, lastName)\n      {fullName.__doc__}")
    print(f"  lastNameFirst(firstName, lastName)\n      {lastNameFirst.__doc__}")
    print("=" * 50)
    print()