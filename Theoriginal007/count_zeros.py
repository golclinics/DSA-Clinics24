def count_zeros(arr):
    """
    Function to count the number of zeros in a list using a linear search algorithm.
    
    Args:
    arr (list): The list of integers to search for zeros.
    
    Returns:
    int: The count of zeros in the list.
    """
    count = 0  # Initialize zero counter
    for num in arr:  # Linear search through the list
        if num == 0:  # If we encounter a zero, increment the count
            count += 1
    return count


def frequency_count(arr):
    """
    Function to count the frequency of each number in the array using a hash map (dictionary).
    
    Args:
    arr (list): The list of integers to search for frequencies.
    
    Returns:
    dict: A dictionary with numbers as keys and their frequency as values.
    """
    freq_map = {}  # Initialize a hash map
    for num in arr:
        if num in freq_map:  # Increment the count if the number exists in the map
            freq_map[num] += 1
        else:
            freq_map[num] = 1  # Add the number to the map if it doesn't exist
    return freq_map


def count_zeros_optimized(arr):
    """
    Optimized function to count the number of zeros using frequency counting for larger datasets.
    
    Args:
    arr (list): The list of integers to search for zeros.
    
    Returns:
    int: The count of zeros in the list.
    """
    freq_map = frequency_count(arr)
    return freq_map.get(0, 0)  # Return the count of zeros or 0 if no zeros are found


def test_algorithms():
    """
    Function to test different data structures and algorithms for counting zeros.
    """
    # Test cases
    test_cases = [
        [1, 0, 2, 0, 3, 0, 4],  # Standard case with zeros
        [0, 0, 0, 0],  # All zeros
        [1, 2, 3, 4],  # No zeros
        [5, 6, 7, 8, 0],  # One zero at the end
        [],  # Empty list
        [0],  # Single zero
        [1] * 1000000 + [0] * 1000000  # Large dataset with one million zeros
    ]
    
    print("Testing Linear Search Algorithm for Counting Zeros:")
    for i, case in enumerate(test_cases):
        result = count_zeros(case)
        print(f"Test case {i + 1}: Found {result} zeros.")
    
    print("\nTesting Optimized Algorithm using Frequency Count for Counting Zeros:")
    for i, case in enumerate(test_cases):
        result = count_zeros_optimized(case)
        print(f"Test case {i + 1}: Found {result} zeros.")


def analyze_complexity():
    """
    Function to provide a basic time complexity analysis of the algorithms.
    """
    print("\nTime Complexity Analysis:")
    
    # For the linear search algorithm
    print("Linear Search Algorithm (count_zeros):")
    print("Time complexity: O(n) - where 'n' is the length of the input array.")
    
    # For the optimized frequency counting algorithm
    print("\nOptimized Algorithm with Frequency Count (count_zeros_optimized):")
    print("Time complexity: O(n) - Building the frequency map takes O(n) and retrieving the count takes O(1).")


if __name__ == "__main__":
    test_algorithms()  # Run the test cases
    analyze_complexity()  # Show the time complexity analysis
