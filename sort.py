from random import randint
from math import floor
from math import log, ceil
from copy import deepcopy

def bubble_sort(l):
    exchanges = True
    count = 0
    while count <= len(l)-1 and exchanges:
        exchanges = False
        for j in range(len(l)-1-count):
            if l[j] > l[j+1]:
                exchanges = True
                l[j], l[j+1] = l[j+1], l[j]
        count += 1
    return l 


def select_sort(l):
    for count in range(len(l)-1):
        max_num = l[0]
        max_loc = 0
        for loc in range(1, len(l)-count):
            if l[loc] > max_num:
                max_num, max_loc = l[loc], loc

        l[max_loc], l[len(l)-1-count] = l[len(l)-1-count], l[max_loc]
    return l


def insert_sort(l):
    for count in range(1, len(l)):
        item = l[count]
        loc = count
        for i in reversed(range(count)):
            if item < l[i]:
                l[loc], l[i] = l[i], l[loc]
                loc = i
            else:
                break
    return l


def gap_insert_sort(l, gap):
    for count in range(gap, len(l)):
        item = l[count]
        loc = count
        for i in reversed(range((count-gap)%gap, count, gap)):
            if item < l[i]:
                l[loc], l[i] = l[i], l[loc]
                loc = i
            else:
                break
    return l

 
def shell_sort(l, gap):
    l = gap_insert_sort(l, gap)
    print(l)
    l = gap_insert_sort(l,1)
    return l


def merge_sort(l):
    
    if len(l) > 1:
        mid = len(l)//2
        left = l[mid:]
        right = l[:mid]
        
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    
    return l


def qsort(l):
    if len(l) <= 1:
        return l
    else:
        left = qsort([lt for lt in l[1:] if lt <= l[0]])
        right = qsort([ge for ge in l[1:] if ge > l[0]])
        return left + [l[0]] + right


def quick_sort(l, first, last):
    if first < last:
        i = first - 1
        for j in range(first, last):
            if l[j] <= l[last]:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i+1], l[last] = l[last], l[i+1]
        
        quick_sort(l, first, i)
        quick_sort(l, i+1, last)
    return l


def bucket_sort(l):
    buckets = [0 for _ in range(min(l), max(l)+1)]
    res = []
    for i in l:
        buckets[i-min(l)] += 1
    
    for j in range(len(buckets)):
        if buckets[j] != 0:
            res.extend(buckets[j] * [j + min(l)])
    
    return res


def bucket_sort_dict(l):
    res, counter = [], {}
    for i in l:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
   
    for i in range(min(l), max(l)+1):
        count = counter.get(i)
        if count is not None:
            res.extend(count * [i])
            
    return res


def count_sort(l):
    pass

def radix_sort_bucket(l, radix=10):
    for i in range(int(ceil(log(max(l), radix)))):
        bucket = [[] for i in range(radix)]
        for j in l:
            bucket[j//(radix**(i)) % radix].append(j)
            
        l = [y for x in bucket for y in x]
    return l


def radix_sort_count(l, radix=10):
    for i in range(int(ceil(log(max(l), radix)))):
        counter = [0 for i in range(10)]
        counter2 = [0 for i in range(10)]
        counter3 = [0 for i in range(10)]
        res = [0 for i in range(len(l))] 
        for j in l:
            counter[j//(radix ** i) % radix] += 1
        counter3 = counter[:]
        for k in range(1, radix):
            counter[k] = counter[k] + counter[k-1]
        counter2 = counter[:]
        for m in l:
            x = m//(radix ** i) % radix
            res[counter2[x] - counter3[x]] = m
            counter3[m//(radix ** i) % radix] -= 1
        l = res
    return l


def heap_sort():
    pass


if __name__ == '__main__':
    data = [randint(0,99) for _ in range(15)]
    print('raw_data:'.ljust(16), data)
    #1 print('bubble_sort:', bubble_sort(data))
    #2 print('select_sort:', select_sort(data))
    #3 print('insert_sort:', insert_sort(data))

    #  print('gap_insert_sort:', gap_insert_sort(data,1))
    #4 print('shell_sort:', shell_sort(data, 3))

    #5 print('merge_sort:', merge_sort(data))
    #  print('qsort:', qsort(data))
    #6 print('quick_sort:', quick_sort(data, 0, len(data)-1))

    #  print('bucket_sort:', bucket_sort(data))
    #  print('count_sort:', count_sort(data))
    #7 print('radix_sort:', radix_sort(data))
    
    #8 print('heap_sort:', heap_sort(data))


 
