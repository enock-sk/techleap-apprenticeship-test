def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Return None if list has fewer than 2 elements

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


# Example usage
print(find_second_largest([10, 5, 8, 12, 3]))  # Output: 10
print(find_second_largest([1, 1, 1]))  # Output: None
print(find_second_largest([5]))  # Output: None