import timeit
import array
import random
import quick_sort


def profile(function, input_array, iterations):
    time = 0
    for i in range(iterations):
        start = timeit.default_timer()
        function(input_array)
        stop = timeit.default_timer()
        time += stop - start
    return time


if __name__ == '__main__':
    sorted_array = [0] * 10
    sorted_array = [i+1  for i in range(30)]

    unsorted_array = [0] * 10
    unsorted_array = [random.randint(1,30)  for i in range(30)]
    print 'time consumed by sorted_array'
    print profile(quick_sort.quick_sort, sorted_array, 100)
    print profile(quick_sort.quick_sort, sorted_array, 1000)
    print profile(quick_sort.quick_sort, sorted_array, 10000)
    print 'time consumed by unsorted_array'
    print profile(quick_sort.quick_sort, unsorted_array, 100)
    print profile(quick_sort.quick_sort, unsorted_array, 1000)
    print profile(quick_sort.quick_sort, unsorted_array, 10000)