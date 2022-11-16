# Heapq
* Priority queue
* The pop always returns the smallest element
* We can push on pop in the same time using `heapq.heappushpop(heap, element)`
* If we use that previous function, the pop will consider the pushed element. If we don't want it to, we can use `heapq.heapreplace(heap, element)`
* If you want to pop the largest element, there's maxheap. It has the same function names than minheap in this following format : `heapq._func_max` where func can be 'heapify' or 'heappop'.
** THIS MAX HEAP IMPLEMENTATION BREAK THE ORDER!**
* U can use -1 * your list to heapify.
