import random
import profiler
import bubble_sort
import insertion_sort
import quick_sort
import heap_sort
import bucket_sort
import merge_sort

def time_compare(function, iterattions):
    flag = 1
    array_size = 500
    best_case = worst_case = avg_case = 0
    for i in range(iterattions):
        c = [0] * array_size
        c = [i for i in range(array_size, 0, -1)] # unsorted

        b = [0] * array_size
        b = [random.randint(1, array_size) for i in range(array_size, 0, -1)]#sorted
        if function.__name__ == 'quickSort':
            if flag == 1:
                a = [0] * array_size
                a = [random.randint(1, array_size) for i in range(array_size, 0, -1)]
                flag = 0
            best_case += profiler.profile(function, a, 1)
            avg_case += profiler.profile(function, b, 1)
            worst_case += profiler.profile(function, c, 1)
        else:
            a = [0] * array_size
            a = [i+1 for i in range(array_size)]

            best_case += profiler.profile(function, a, 1)
            avg_case += profiler.profile(function, b, 1)
            worst_case += profiler.profile(function, c, 1)
    print  function.__name__,"\t\t ", best_case, "\t\t", avg_case, "\t\t", worst_case

if __name__ == '__main__':
    iterattions = 1000
    print "  \t\t\t\tBest case \t\t Avg case\t\t\tworst case"
    time_compare(quick_sort.quick_sort, iterattions)
    time_compare(bubble_sort.bubble_sort, iterattions)
    time_compare(merge_sort.merge_sort, iterattions)
    time_compare(heap_sort.heap_sort, iterattions)
    time_compare(insertion_sort.insertion_sort, iterattions)
    time_compare(bucket_sort.bucket_sort, iterattions)
