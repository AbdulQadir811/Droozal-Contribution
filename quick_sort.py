def quick_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        i = 0
        pivot = arr[0]
        for j in range(0, len(arr)-1):
            if arr[j+1] < pivot:
                arr[i + 1], arr[j + 1] = arr[j + 1], arr[i + 1]
                i = i+1
        arr[0], arr[i] = arr[i], arr[0]
        x = quick_sort(arr[:i])
        y = quick_sort(arr[i+1:])
        x.append(arr[i])
        return x + y


if __name__ == '__main__':
    arr = [1, 0, 3, 5, 9, 6, 7, 8]
    print(quick_sort(arr))
