# Original code and its issues
"""
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)
"""

# Issues:
# 1. What's wrong:
#    - The code modifies the list (numbers) while iterating over it using range(len(numbers)).
#    - Removing elements shifts the indices, causing the loop to skip elements.
#    - The condition `i % 2 == 0` checks if the *index* is even, not the value, so it removes elements at even indices (0, 2, 4), not even numbers.
#
# 2. Output:
#    - Initial list: [1, 2, 3, 4, 5]
#    - i=0: remove 1 → [2, 3, 4, 5]
#    - i=1: remove 3 → [2, 4, 5]
#    - i=2: remove 5 → [2, 4]
#    - Output: [2, 4]
#
# 3. Fixed code to remove even numbers:
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Example usage
numbers = [1, 2, 3, 4, 5]
print(remove_even_numbers(numbers))  # Output: [1, 3]

# Alternative iterative solution:
def remove_even_numbers_iterative(numbers):
    result = numbers.copy()  # Avoid modifying original list
    i = 0
    while i < len(result):
        if result[i] % 2 == 0:
            result.pop(i)
        else:
            i += 1
    return result

# Example usage
print(remove_even_numbers_iterative([1, 2, 3, 4, 5]))  # Output: [1, 3]