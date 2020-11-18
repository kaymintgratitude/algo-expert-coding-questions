def heapSort(array):
    buildHeap(array)
    start = 0
    end = len(array) - 1

    while end >= start:
        print(f"Removing: {array[start]}")
        swap(start, end, array)
        print(f"After swapping: {array}")
        end -= 1
        print(f"Before sift start: {start} | end {end}")
        siftDown(array, start, end)
        print(f"After sifting down: {array}")

    return array


def buildHeap(array):
    # parentIdx = (len(array) - 2) // 2
    # for i in reversed(range(parentIdx + 1)):
    # 	siftDown(array, i, len(array)-1)
    for i in reversed(range(len(array))):
        siftDown(array, i, len(array) - 1)
        print(f"buildHeap: {array}")
    return array


def siftDown(array, start, end):
    n = end
    if start <= end:
        left = 2 * start + 1
        right = 2 * start + 2
        if left <= n:
            max_child = left
            if right < n and array[right] > array[left]:
                max_child = right
            if array[start] < array[max_child]:
                swap(max_child, start, array)
                siftDown(array, max_child, end)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    return array


def main():
    input_array = [8, 5, 2, 9, 5, 6, 3]
    print(heapSort(input_array))


if __name__ == "__main__":
    main()