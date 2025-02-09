#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to print an array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Merge Sort Implementation
void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Quick Sort Implementation
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to measure execution time
void measureExecutionTime(void (*sortFunction)(int[], int, int), int arr[], int n) {
    clock_t start, end;
    start = clock();
    sortFunction(arr, 0, n - 1);
    end = clock();
    printf("Execution time: %f ms\n", ((double)(end - start) / CLOCKS_PER_SEC) * 1000);
}

int main() {
    int n = 10000;
    int *arr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }

    printf("Original Array (First 100 Elements):\n");
    printArray(arr, 100);

    printf("\nMerge Sort:\n");
    measureExecutionTime(mergeSort, arr, n);
    printf("Sorted Array (First 100 Elements):\n");
    printArray(arr, 100);
    
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }

    printf("\nOriginal Array (First 100 Elements):\n");
    printArray(arr, 100);
    
    printf("\nQuick Sort:\n");
    measureExecutionTime(quickSort, arr, n);
    printf("Sorted Array (First 100 Elements):\n");
    printArray(arr, 100);
    
    free(arr);
    return 0;
}
