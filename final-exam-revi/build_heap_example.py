def max_heapify(heap_list, cur_i):
    if left(cur_i) < len(heap_list) and heap_list[left(cur_i)] > heap_list[cur_i]:
        largest = left(cur_i)
    else:
        largest = cur_i
    if right(cur_i) < len(heap_list) and heap_list[right(cur_i)] > heap_list[largest]:
        largest = right(cur_i)
    if largest != cur_i:
        heap_list[cur_i], heap_list[largest] = heap_list[largest], heap_list[cur_i]
        max_heapify(heap_list, largest)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_max_heap(heap_list):
    n = int((len(heap_list)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(heap_list, i)


heap_in = [3, 6, 2, 1, 4, 5, 10, 15, 22]
build_max_heap(heap_in)
print(heap_in)
