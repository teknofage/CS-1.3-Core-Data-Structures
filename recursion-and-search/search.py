#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len():
        return None
    elif array[index] == item: #we found it!
        return index
    return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    if item == array[0]:
        return 0
    else:
        left = 0 #left pointer = first item in array
        right = len(array) - 1 #right pointer = last item in array
        while left <= right:
            middle_index = (left + right) // 2 # find the middle
            if item == array[middle_index]:
                return middle_index
            elif item < array[middle_index]:
                # move my pointers
                right = middle_index -1
            elif item > array[middle_index]:
                # move my pointers
                right = middle_index + 1
            else:
                return None
        return None
                


def binary_search_recursive(array, item, left=None, right=None):
    left = 0
    right = len(array) -1
    return recursive_helper(array, item, left, right)

def recursive_helper(array, item, left, right):
    middle_index = (left + right) // 2
    if (left > right):
        return None
    if array[middle_index] == item:
        return middle_index
    elif item < array[middle_index]:
        return recursive_helper(array, item, left, middle_index - 1)
    else:
        return recursive_helper(array, item, middle_index + 1, right)
    
    return binary_search_recursive(array, item, left, right)