"""
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)
"""

def remove_even_numbers(numbers):
    """Return a new list with even numbers removed."""
    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5]
print(remove_even_numbers(numbers))  # Output: [1, 3]

def remove_even_numbers_iterative(numbers):
    """Remove even numbers using a loop (without modifying while iterating)."""
    result = numbers.copy()
    i = 0
    while i < len(result):
        if result[i] % 2 == 0:
            result.pop(i)
        else:
            i += 1
    return result

print(remove_even_numbers_iterative([1, 2, 3, 4, 5]))  # Output: [1, 3]
