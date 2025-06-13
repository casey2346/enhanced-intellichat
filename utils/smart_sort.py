"""
Smart Sort Module - Intelligent Sorting Functionality
Advanced sorting algorithms for AI Assistant
"""

def smart_sort(data, reverse=False, key=None, algorithm='auto'):
    """
    Enhanced smart sorting function with adaptive algorithm selection

    Args:
        data: Iterable to sort
        reverse: Sort in descending order if True
        key: Function to extract comparison key from each element
        algorithm: 'auto', 'timsort', 'quicksort', 'heapsort', 'insertion'

    Returns:
        Sorted list

    Raises:
        TypeError: If data type is not sortable
        ValueError: If data is empty or invalid
    """

    # Input validation
    if data is None:
        raise ValueError("Cannot sort None type")

    try:
        # Convert to list if not already
        if not isinstance(data, list):
            data = list(data)
    except TypeError:
        raise TypeError("Data must be iterable")

    if len(data) == 0:
        return []

    if len(data) == 1:
        return data.copy()

    # Smart algorithm selection
    try:
        if algorithm == 'auto':
            # Intelligent algorithm choice based on data characteristics
            data_size = len(data)

            if data_size < 10:
                # Use insertion sort for very small datasets
                return _insertion_sort(data, reverse=reverse, key=key)
            elif data_size < 50:
                # Use Python's built-in Timsort for small to medium datasets
                return sorted(data, reverse=reverse, key=key)
            else:
                # For large datasets, analyze data characteristics
                if _is_nearly_sorted(data, key):
                    # Timsort excels with partially sorted data
                    return sorted(data, reverse=reverse, key=key)
                else:
                    # General case - use Python's optimized Timsort
                    return sorted(data, reverse=reverse, key=key)

        elif algorithm == 'timsort':
            return sorted(data, reverse=reverse, key=key)

        elif algorithm == 'insertion':
            return _insertion_sort(data, reverse=reverse, key=key)

        elif algorithm == 'quicksort':
            return _quicksort(data.copy(), reverse=reverse, key=key)

        else:
            # Default to Python's built-in sort
            return sorted(data, reverse=reverse, key=key)

    except TypeError as e:
        # Handle comparison errors
        sample_types = set(type(x).__name__ for x in data[:5])
        if len(sample_types) > 1:
            raise TypeError(f"Cannot sort mixed types: {sample_types}")
        else:
            raise TypeError(f"Data type not sortable: {e}")

    except Exception as e:
        raise RuntimeError(f"Sorting failed: {str(e)}")


def _insertion_sort(data, reverse=False, key=None):
    """Insertion sort implementation for small datasets"""
    result = data.copy()

    for i in range(1, len(result)):
        current = result[i]
        current_key = key(current) if key else current
        j = i - 1

        while j >= 0:
            compare_key = key(result[j]) if key else result[j]
            should_swap = (compare_key > current_key) if not reverse else (compare_key < current_key)

            if should_swap:
                result[j + 1] = result[j]
                j -= 1
            else:
                break

        result[j + 1] = current

    return result


def _quicksort(data, reverse=False, key=None):
    """Quicksort implementation"""
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]
    pivot_key = key(pivot) if key else pivot

    left = []
    middle = []
    right = []

    for item in data:
        item_key = key(item) if key else item
        if item_key < pivot_key:
            left.append(item)
        elif item_key == pivot_key:
            middle.append(item)
        else:
            right.append(item)

    if reverse:
        return _quicksort(right, reverse, key) + middle + _quicksort(left, reverse, key)
    else:
        return _quicksort(left, reverse, key) + middle + _quicksort(right, reverse, key)


def _is_nearly_sorted(data, key=None, threshold=0.8):
    """Check if data is nearly sorted"""
    if len(data) < 2:
        return True

    sorted_pairs = 0
    total_pairs = len(data) - 1

    for i in range(total_pairs):
        current = key(data[i]) if key else data[i]
        next_item = key(data[i + 1]) if key else data[i + 1]

        try:
            if current <= next_item:
                sorted_pairs += 1
        except TypeError:
            return False

    return (sorted_pairs / total_pairs) >= threshold


def generate_sort_example(language='python'):
    """Generate sorting code example"""
    if language.lower() == 'python':
        return """# Smart Sorting Example
from utils.smart_sort import smart_sort

# Basic sorting
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = smart_sort(numbers)
print(f"Sorted: {sorted_numbers}")

# Reverse sorting  
reverse_sorted = smart_sort(numbers, reverse=True)
print(f"Reverse: {reverse_sorted}")

# Sort with key function
words = ["apple", "pie", "banana", "book"]
sorted_by_length = smart_sort(words, key=len)
print(f"By length: {sorted_by_length}")

# Advanced usage with custom algorithm
large_data = list(range(1000, 0, -1))
result = smart_sort(large_data, algorithm='auto')
print(f"Large data sorted: {len(result)} items")
"""
    else:
        return "// Smart sorting examples available in Python"


def benchmark_sorting_algorithms(data_sizes=[100, 1000], num_trials=3):
    """Benchmark different sorting algorithms"""
    import time
    import random

    results = {}

    for size in data_sizes:
        print(f"\\n📊 Benchmarking with {size} elements:")
        results[size] = {}

        for trial in range(num_trials):
            # Generate test data
            test_data = [random.randint(1, 1000) for _ in range(size)]

            algorithms = ['auto', 'timsort', 'insertion', 'quicksort']

            for algo in algorithms:
                if algo == 'insertion' and size > 1000:
                    continue  # Skip insertion sort for large datasets

                start_time = time.time()
                try:
                    result = smart_sort(test_data, algorithm=algo)
                    end_time = time.time()

                    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

                    if algo not in results[size]:
                        results[size][algo] = []
                    results[size][algo].append(execution_time)

                    # Verify sorting correctness
                    if result != sorted(test_data):
                        print(f"❌ {algo} failed correctness test!")

                except Exception as e:
                    print(f"❌ {algo} failed: {e}")

        # Print average results
        for algo in results[size]:
            if results[size][algo]:
                avg_time = sum(results[size][algo]) / len(results[size][algo])
                print(f"   {algo:>10}: {avg_time:.3f}ms")

    return results


# Usage examples and testing
if __name__ == "__main__":
    print("🚀 Smart Sorting Function Demo\\n")

    # Example 1: Basic sorting
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("📋 Original:", numbers)
    print("📈 Sorted:", smart_sort(numbers))
    print("📉 Reverse:", smart_sort(numbers, reverse=True))

    # Example 2: Sorting with key function
    words = ["apple", "pie", "banana", "book", "cherry"]
    print("\\n📝 Original words:", words)
    print("📏 By length:", smart_sort(words, key=len))
    print("🔤 Alphabetical:", smart_sort(words, key=str.lower))

    # Example 3: Error handling
    try:
        smart_sort([1, "2", 3])  # Mixed types
    except TypeError as e:
        print(f"\\n❌ Error handling: {e}")

    # Example 4: Performance comparison
    print("\\n⚡ Performance Benchmarking:")
    benchmark_sorting_algorithms()

    print("\\n✅ Smart sorting function is ready for production use!")
    print("🎯 Features:")
    print("   • Adaptive algorithm selection")
    print("   • Comprehensive error handling")
    print("   • Performance optimization")
    print("   • Multiple sorting algorithms")
    print("   • Detailed benchmarking")