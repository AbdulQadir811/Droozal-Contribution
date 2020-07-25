def BinarySearch(list1, x):
    if len(list1) == 0:
        print 'list is empty'
        return None
    lists2 = list1[:]
    BubbleSort(list1)
    b = len(list1)
    a = 0
    if len(list1) % 2 == 0:
        c = b / 2
    else:
        c = (b+1) / 2
    flag = 0
    while((c != 0) or (flag == 0)):
            flag = 1
            mid = (a + b) / 2
            if list1[mid] < x:
                    a = mid
            elif list1[mid] > x:
                    b = mid
            if list1[mid] == x:
                print x, 'found'
                j = 0
                for i in lists2:
                    if lists2[j] == x:
                        return j
                    j = j + 1
            c = c - 1
    print x, ' not found'


def BubbleSort(list1):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                d = swap(list1[j], list1[j+1])
                list1[j] = d[0]
                list1[j+1] = d[1]
    return list1


def swap(a, b):
    a, b = b, a
    d = [a, b]
    return d


if __name__ == '__main__':
    list1 = []
    BinarySearch(list1, 1)
