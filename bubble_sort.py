def bubble_sort(list1):
    swapped = 0
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                d = swap(list1[j], list1[j+1])
                list1[j] = d[0]
                list1[j+1] = d[1]
                swapped = 1
            if swapped == 0:
                return list1
    return list1


def swap(a, b):
    a, b = b, a
    d = [a, b]
    return d


def palindrome_checker(my_string):
    flag = 0
    n = len(my_string)
    j = n
    for i in range(0, n / 2):
        j = j - 1
        if my_string[j] != my_string[i]:
            flag = 1
            break
    if flag == 1:
        print my_string, 'is not palindrome'
    else:
        print my_string, 'is palindrome'


if __name__ == '__main__':
    my_string = "noon"
    list1 = [5, 1, 4, 2, 8]
    bubble_sort(list1)
    print(list1)
    print(swap(3, 4))
    palindrome_checker(my_string)
