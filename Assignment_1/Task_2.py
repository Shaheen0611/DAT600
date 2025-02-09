# Modified Python code to print the sorted array

import numpy as np
import time

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort implementation
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to measure execution time
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        sort_function(arr, 0, len(arr) - 1)
    else:
        sort_function(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

# Function to print an array
def print_array(arr, name):
    print(f"{name} Sorted Array:")
    print(arr[:100])  # Print only the first 100 elements for readability

# Using the same input size as in the C program (n = 10000)
n = 10000
arr = np.random.randint(0, 10000, size=n).tolist()

# Measure execution time for Merge Sort
merge_arr = arr.copy()
print("Original Array (First 100 Elements):")
print(merge_arr[:100])  # Print a sample of the original array

merge_time = measure_execution_time(merge_sort, merge_arr)
print_array(merge_arr, "Merge Sort")

# Measure execution time for Quick Sort
quick_arr = arr.copy()
quick_time = measure_execution_time(quick_sort, quick_arr)
print_array(quick_arr, "Quick Sort")

# Display execution times
print(f"\nExecution Time for Merge Sort: {merge_time:.3f} ms")
print(f"Execution Time for Quick Sort: {quick_time:.3f} ms")
