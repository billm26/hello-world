"""Examples of sorting a list in Python."""


def sort_basic():
    """Sort a list of numbers using sorted() and .sort()."""
    numbers = [5, 2, 8, 1, 9, 3]

    # sorted() returns a new sorted list
    sorted_numbers = sorted(numbers)
    print("sorted():", sorted_numbers)  # [1, 2, 3, 5, 8, 9]

    # .sort() sorts the list in place
    numbers.sort()
    print(".sort():", numbers)  # [1, 2, 3, 5, 8, 9]


def sort_reverse():
    """Sort a list in descending order."""
    numbers = [5, 2, 8, 1, 9, 3]
    sorted_desc = sorted(numbers, reverse=True)
    print("Reverse:", sorted_desc)  # [9, 8, 5, 3, 2, 1]


def sort_with_key():
    """Sort using a key function."""
    words = ["banana", "apple", "cherry"]
    sorted_by_length = sorted(words, key=len)
    print("By length:", sorted_by_length)  # ['apple', 'banana', 'cherry']


def sort_dicts():
    """Sort a list of dictionaries by a specific field."""
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    sorted_people = sorted(people, key=lambda p: p["age"])
    print("By age:", sorted_people)


if __name__ == "__main__":
    sort_basic()
    sort_reverse()
    sort_with_key()
    sort_dicts()
