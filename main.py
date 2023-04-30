# Exercise 1

def power(a: int, b: int):
    print(f"The function is called with {a} & {b}-> Winding")
    # base case - to tell our function when to stop
    if b == 0:
        return 1  # 1 would be the outcome if you would carry out the operation
    elif a < 0 or b < 0:  # setting the case if both are below 0
        print("Base case reached returning 1")
        return -1
    else:
        return_value = a * power(a, b - 1)  # multiplying a with itself as often as needed
        print(f"The function({a} & {b}) returns {return_value} -> Unwinding")
    return return_value

# Exercise 2


def binary_search(numbers: list, num: int):
    numbers.sort()  # only works for sorted lists, so we're sorting here
    mid = len(numbers) // 2
    middle = numbers[mid]  # to make the code easier to read I'm adding a variable that takes care of the indexing
    # base case:
    if len(numbers) == 1:  # if the length of the list is just 1, we only need to check that one value
        if middle == num:  # if it is the same, return the index, otherwise we'll get an error (-1)
            return mid
        else:
            return -1
    else:
        if middle == num:  # if the middle is the same as the num, return the index
            return mid
        elif middle > num:
            # if the middle is higher than the number, we need to search the left until we hit the middle
            # going from the start of the list to the middle through slicing
            # recursion makes the remaining list smaller with every time it's called
            result = binary_search(numbers[:mid], num)
            return result
        else:  # the middle would be smaller than num
            # if the middle is lower, we need to search the right side
            # going from the middle of the list to the end through slicing
            # recursion makes the remaining list smaller with every time it's called
            result = binary_search(numbers[mid:], num)
            return mid + result
            # I need to add the mid to the result, as I want the index if we look at the list as a whole and not just
            # the part where I've already split it - if I did not have that statement it could easily return the index
            # 1, even though in the sorted list sth else has that index


numb = [1, 2, 5, 4, 3]

print(binary_search(numb, 2))
print(binary_search(numb, 4))
# I ran into the issue described above here - the function would return index 1 when searching for the number 4,
# as it wasn't going from the index of the original list
