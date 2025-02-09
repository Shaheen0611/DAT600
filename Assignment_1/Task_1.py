import numpy as np
import matplotlib.pyplot as plt
import time

# Step-counting wrapper function
class StepCounter:
    def __init__(self):
        self.steps = 0

    def count(self):
        self.steps += 1

# Insertion Sort
def insertion_sort(arr, step_counter=None):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        if step_counter: step_counter.count()
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if step_counter: step_counter.count()
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr, step_counter=None):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        if step_counter: step_counter.count()
        
        merge_sort(L, step_counter)
        merge_sort(R, step_counter)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if step_counter: step_counter.count()
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            if step_counter: step_counter.count()
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            if step_counter: step_counter.count()
            arr[k] = R[j]
            j += 1
            k += 1

# Heap Sort
def heapify(arr, n, i, step_counter=None):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        if step_counter: step_counter.count()
        heapify(arr, n, largest, step_counter)

def heap_sort(arr, step_counter=None):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, step_counter)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, step_counter)
        if step_counter: step_counter.count()

# Quick Sort
def quick_sort(arr, low, high, step_counter=None):
    if low < high:
        pi = partition(arr, low, high, step_counter)
        quick_sort(arr, low, pi - 1, step_counter)
        quick_sort(arr, pi + 1, high, step_counter)

def partition(arr, low, high, step_counter=None):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if step_counter: step_counter.count()
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if step_counter: step_counter.count()
    return i + 1

# Running experiments for different input sizes
sizes = [10, 50, 100, 200, 500, 1000]
sorting_algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Quick Sort": lambda arr, sc: quick_sort(arr, 0, len(arr) - 1, sc)
}
step_counts = {alg: [] for alg in sorting_algorithms}

for n in sizes:
    for name, algo in sorting_algorithms.items():
        step_counter = StepCounter()
        test_array = np.random.randint(0, 1000, size=n).tolist()
        algo(test_array, step_counter)
        step_counts[name].append(step_counter.steps)

# Plotting the step counts
plt.figure(figsize=(10, 6))
for name, steps in step_counts.items():
    plt.plot(sizes, steps, marker='o', label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Number of Steps vs Input Size for Sorting Algorithms")
plt.legend()
plt.grid(True)
plt.show()

# Adjusting function call for Quick Sort
def measure_time_fixed(sort_func, arr):
    start_time = time.time()
    if sort_func == sorting_algorithms["Quick Sort"]:
        sort_func(arr.copy(), None)  # Quick Sort requires an extra argument
    else:
        sort_func(arr.copy())
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

execution_times_fixed = {alg: [] for alg in sorting_algorithms}

for n in sizes:
    for name, algo in sorting_algorithms.items():
        test_array = np.random.randint(0, 1000, size=n).tolist()
        exec_time = measure_time_fixed(algo, test_array)
        execution_times_fixed[name].append(exec_time)

# Plot execution times
plt.figure(figsize=(10, 6))
for name, times in execution_times_fixed.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time vs Input Size for Sorting Algorithms (Python)")
plt.legend()
plt.grid(True)
plt.show()
