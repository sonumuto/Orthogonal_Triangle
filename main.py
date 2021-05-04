# Python 3.8
# Samet Umut Yigitoglu


def read_file(file_path: str) -> [int]:
    """
    Read the file given by the path
    :param file_path: File path
    :return: Integer array of elements
    """
    file = open(file_path)
    array = file.read().split()
    int_array = [int(i) for i in array]
    file.close()
    return int_array


def is_prime(value: int) -> bool:
    """
    Checks if the given value is prime
    :param value: Value as an integer
    :return: Boolean value that is True if the given value is prime
    """
    if value >= 2:
        for i in range(2, value // 2 + 1):
            if value % i == 0:
                return False
    return True


def find_max_sum(triangle_array: [int]) -> int:
    """
    This function finds the maximum sum of the orthogonal triangle according to the rules below:
        1. Start from the top and move downwards and diagonally
        2. Only allowed to walk downwards and diagonally
        3. Only walk over non-prime numbers
        4. Reach at the end of the pyramid as much as possible
        5. Treat your input as a pyramid

    :param triangle_array: Array that contains all the elements of the orthogonal triangle
    :return: Maximum sum according to given rules
    """
    max_sum = triangle_array[0]  # Top element
    layer = 2 # Current layer
    first_element = 1 # First element's index of the current layer
    current_element = 0
    while first_element < len(triangle_array):
        if is_prime(triangle_array[first_element + current_element + 1]) and is_prime(triangle_array[first_element + current_element + 1]):
            return max_sum
        elif is_prime(triangle_array[first_element + current_element + 1]):
            max_sum += triangle_array[first_element + current_element]
        elif is_prime(triangle_array[first_element + current_element]):
            max_sum += triangle_array[first_element + current_element + 1]
            current_element += 1
        elif triangle_array[first_element + current_element] > triangle_array[first_element + current_element + 1]:
            max_sum += triangle_array[first_element + current_element]
        else:
            max_sum += triangle_array[first_element + current_element + 1]
            current_element += 1

        first_element += layer
        layer += 1
    return max_sum


if __name__ == '__main__':
    print(find_max_sum(read_file("input.txt")))
