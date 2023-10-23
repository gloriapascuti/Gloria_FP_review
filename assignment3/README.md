# This is assignment 3
## We will use especially assignment 2 and it's complexity

## Requirements:
#### Calculate the complexity of the sorting algorithms you've implemented for the previous assignment. You may use additional resources for help, but you have to understand and be able to explain the complexity for both the best case as well as worst case. You can show this on screen or written on paper.
#### Update the program created for the previous assignment by adding the following three additional menu entries -- one for best case, one for average case and the last one for worst case. When the user selects one of these, the program will time and illustrate the runtime of the implemented algorithms by sorting 5 data structures, each having twice the number of elements of the previous one. The elements of the data structure must be in accordance with the current case. See the example below.

## Example:
#### Let's say that as part of A2 you've implemented BubbleSort and ShellSort. Let's say the user wishes to see the behaviour of these algorithms in the worst case. Your program will generate five lists (e.g., lenghts 500, 1000, 2000, 4000 and 8000 elements) in which elements are in worst case configuration (for bubble sort, this happens if the list is already sorted, but in reverse). Then, you will time how long it takes to sort each list using a module such as timeit, and display the results on the console.
#### In case the algorithm takes too long/little, you can adjust the list lengths (e.g., permutation sort)
#### Make sure that all calls to the sorting algorithms use the same input lists.
#### Make sure the sorting algorithms do not perform additional work (e.g., displaying on the console, as required for A2)
#### Display the results (list length, sort duration) in a way that allows users to see the progression of the runtime.


## Time complexity for Cocktail Sort 
#### Cocktails sort, also known as bidirectional bubble sort, is a variation of the bubble sort algorithm. It works by repeatedly moving through the list from left to right and then from right to left, comparing elements and swapping them if they are in the wrong order.
### The worst case time complexity of cocktail sort is O(n^2) for a list of n elements aka when the list is in reverse.
### When the list of n elements is already sorted is the best case time complexity of cocktail sort.

## Time complexity for Heap Sort
#### Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a binary max-heap or min-heap. It then swaps the root element (which is the maximum element for max-heap and the minimum element for min-heap) with the last element in the heap, reduces the heap size, and heapifies the root element to maintain the heap property. It repeats this process until the heap is empty, resulting in a sorted array.
### The worst time complexity for heap sort is O(n*logn), or we can say that when the input list is in reverse order.
### When the list is already heapified, also a O(n*logn) complexity, it's the best case time complexity for heap sort.
