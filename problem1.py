"""Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start, end):
    """
    Create a list of numbers from start to end (inclusive).

    Args:
        start (int): Starting number
        end (int): Ending number

    Returns:
        list: List of numbers from start to end

    Example:
        >>> create_number_list(1, 5)
        [1, 2, 3, 4, 5]
    """
    #  Implement this function
    # Hint: Use range() and convert to list
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)

    return numbers

def filter_even_numbers(numbers):
    """
    Return a new list containing only the even numbers.

    Args:
        numbers (list): List of integers

    Returns:
        list: List of even numbers only

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Implement this function
    # You can use a loop or list comprehension
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers


def square_numbers(numbers):
    """
    Return a new list with each number squared.

    Args:
        numbers (list): List of numbers

    Returns:
        list: List where each element is squared

    Example:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # TODO: Implement this function
    # Hint: Try a list comprehension!
    sqr_number = []
    for i in numbers:
        sqr_number.append(pow(i,2))

    return sqr_number


def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)

    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
        (9, 1)
    """
    # TODO: Implement this function
    # You can use max() and min() built-in functions
    max_number = max(numbers)
    min_number = min(numbers)
    
    return (max_number, min_number)


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.

    Args:
        items (list): List that may contain duplicates

    Returns:
        list: List with duplicates removed

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    # Hint: You can use a loop and check if item is already in result list
    # Or convert to set and back to list (but this doesn't preserve order)
    clean_list = set(items)

    return list(clean_list)


def merge_lists(list1, list2):
    """
    Merge two lists, alternating elements from each.
    If one list is longer, append remaining elements.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Merged list with alternating elements

    Example:
        >>> merge_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_lists([1, 2], [10, 20, 30, 40])
        [1, 10, 2, 20, 30, 40]
    """
    # TODO: Implement this function
    # Hint: Use a loop with index, handle different lengths
    merged_list = []
    min_len = min(len(list1), len(list2))
        
    # add elements alternately from both lists
    for i in range(min_len):
        merged_list.append(list1[i])
        merged_list.append(list2[i])

    # add remaining elements from the longer list
    if len(list1) > min_len:
        merged_list.extend(list1[min_len:])
    if len(list2) > min_len:
        merged_list.extend(list2[min_len:])

    return merged_list


def list_statistics(numbers):
    """
    Calculate statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with keys 'sum', 'average', 'count', 'max', 'min'

    Example:
        >>> list_statistics([1, 2, 3, 4, 5])
        {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    """
    if not numbers:
        return None

    # TODO: Implement this function
    # Calculate and return a dictionary with the statistics
    tot_sum = sum(numbers) 
    n_average = tot_sum/len(numbers)
    n_count = len(numbers)
    n_max = max(numbers)
    n_min = min(numbers)
    
    my_dictionary = {'sum':tot_sum, 'average':n_average, 'count':n_count, 'max':n_max, 'min':n_min}

    return my_dictionary


def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size.

    Args:
        items (list): List to split
        chunk_size (int): Size of each chunk

    Returns:
        list: List of lists (chunks)

    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    # TODO: Implement this function
    # Hint: Use list slicing in a loop
    chunked_list = []
    i = 0

    while i < len(items):
        chunked_list.append(items[i:i + chunk_size]) #Slice includes the start index, but excludes the end index
        i += chunk_size

    return chunked_list


# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")