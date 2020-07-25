import math


def bucket_sort(alist):
    length = len(alist)
    if length == 0:
        print 'list is empty'
        return alist
    largest = max(alist)
    if largest < length:
        x = largest
        size = math.ceil(largest / x)
    else:
        size = math.ceil(largest / length)

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j < length:
            buckets[j].append(alist[i])
        elif j >= length:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(len(alist)):
        result += buckets[i]

    return result


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


if __name__ == '__main__':
    alist = [0, 2, 1]
    print bucket_sort(alist)

