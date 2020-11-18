def findThreeLargestNumbers(array):
    if len(array) < 2:
        return array
    largest_three = sort_first_three(array)
    if len(largest_three) <= 2:
        return largest_three

    print(largest_three)

    for i in range(3, len(array)):
        j = 3
        while j > 0 and array[i] > largest_three[j-1]:
            j -= 1
            print(f"Curr: {i} Largest: {j}")

        if j <= 2:
            largest_three.insert(j, array[i])
            largest_three.pop()

    return largest_three


def sort_first_three(array):
    first, second = (
        (array[0], array[1]) if array[0] > array[1] else (array[1], array[0])
    )
    largest_three = [first, second]
    if len(array) < 3:
        return largest_three
    third = array[2]

    curr_index = 0
    while third < array[curr_index]:
        curr_index += 1

    largest_three.insert(curr_index, third)
    return largest_three


def run():
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))


if __name__ == "__main__":
    run()