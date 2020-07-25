def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    if n == 0:
        print 'list is empty'
        return arr
    for i in range(n/2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, -1, -1):
        if i == 0:
            return arr
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = []
    print heapSort(arr)
