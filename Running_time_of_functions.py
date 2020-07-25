import random
import profiler
import Bubble_Sort
import insertionsort
import QuickSort
import heapsort
import Bucket_sort
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
         
    print   function.__name__,"\t\t ", best_case, "\t\t", avg_case, "\t\t", worst_case
    

if __name__ == '__main__':
    iterattions = 1000
    print "  \t\t\t\tBest case \t\t Avg case\t\t\tworst case"
    time_compare(QuickSort.quickSort, iterattions)
    time_compare(Bubble_Sort.BubbleSort, iterattions)
    time_compare(merge_sort.mergeSort, iterattions)
    time_compare(heapsort.heapSort, iterattions)
    time_compare(insertionsort.insertionSort, iterattions)
    time_compare(Bucket_sort.bucket_sort, iterattions)
