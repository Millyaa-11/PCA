def max_heap(heap_list, cur_index):
    if child_left(cur_index) < len(heap_list) and heap_list[child_left(cur_index)] > heap_list[cur_index]:
        largest = child_left(cur_index)
    else:
        largest = cur_index
    if child_right(cur_index) < len(heap_list) and heap_list[child_right(cur_index)] > heap_list[largest]:
        largest = child_right(cur_index)
    if cur_index != largest:
        heap_list[cur_index], heap_list[largest] = heap_list[largest], heap_list[cur_index]
        max_heap(heap_list, largest)


def child_left(i):
    return i * 2 + 1


def child_right(i):
    return i * 2 + 2


def build_heap(heap_list):
    n = (len(heap_list)//2)-1
    for i in range(n, -1, -1):
        max_heap(heap_list, i)


heap_in = [99, 1, 55, 16, 28, 33, 599, 19, 0]
build_heap(heap_in)
print(heap_in)

