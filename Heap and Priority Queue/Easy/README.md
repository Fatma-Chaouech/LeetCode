# Heapq
* Priority queue
* The pop always returns the smallest element
* You can push and pop in the same time using `heapq.heappushpop(heap, element)`
* If you use that heappushpop function, the pop will consider the pushed element (i.e. if it's the smallest, it'll get popped out of the heapq). If you don't want that to happen, you can use `heapq.heapreplace(heap, element)`
* If you want to pop the largest element, there's maxheap. Its functions : `heapq._func_max` where func can be 'heapify' or 'heappop'.
** THIS MAX HEAP IMPLEMENTATION BREAK THE ORDER!**
* You can use instead -1 * your list to heapify.
