def bubble_sort(arr):
    """Bubble Sort implementation."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    """Insertion Sort implementation."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    """Selection Sort implementation."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    original = [64, 25, 12, 22, 11]
    print("Original array:", original)

    # Bubble Sort
    arr = original.copy()
    bubble_sort(arr)
    print("\nBubble Sort result:", arr)

    # Insertion Sort
    arr = original.copy()
    insertion_sort(arr)
    print("\nInsertion Sort result:", arr)

    # Selection Sort
    arr = original.copy()
    selection_sort(arr)
    print("\nSelection Sort result:", arr)
