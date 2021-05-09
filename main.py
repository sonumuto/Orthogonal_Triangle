# Python 3.8
# Samet Umut Yigitoglu


class Element:
    def __init__(self, value):
        self.value = value
        self.prime = is_prime(value)
        self.max_sum = value

    def get_max_sum(self) -> int:
        return self.max_sum

    def add_max_sum(self, new_sum: int):
        self.max_sum += new_sum

    def get_prime(self) -> int:
        return self.prime

    def get_value(self) -> int:
        return self.value


def read_file(file_path: str) -> [Element]:
    """
    Read the file given by the path

    :param file_path: File path
    :return: Integer array of elements
    """
    file = open(file_path)
    array = file.read().split()
    int_array = [Element(int(i)) for i in array]
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


def find_max_sum(triangle_array: [Element]) -> int:
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
    layer = 1  # Current layer
    first_element = 0  # First element's index of the current layer

    # Find the second last layer
    while first_element + 2 * layer + 1 < len(triangle_array):
        first_element += layer
        layer += 1

    while layer > 0:
        for i in range(layer):
            current_element = triangle_array[first_element + i]  # Current element
            left_adjacent = triangle_array[first_element + i + layer]  # Current element's left diagonal adjacent
            right_adjacent = triangle_array[first_element + i + layer + 1]  # Current element's right diagonal adjacent

            # Check if the current element is not prime
            if not current_element.get_prime():
                # Check if both of the adjacents is not prime
                if left_adjacent.get_prime() and right_adjacent.get_prime():
                    pass
                # If both of the adjacents is not prime, find which adjacent has a bigger max_sum
                elif not left_adjacent.get_prime() and not right_adjacent.get_prime():
                    current_element.add_max_sum(max(left_adjacent.get_max_sum(), right_adjacent.get_max_sum()))
                # If the left adjacent is prime, add max_sum of the right adjacent
                elif left_adjacent.get_prime():
                    current_element.add_max_sum(right_adjacent.get_max_sum())
                # If the right adjacent is prime, add max_sum of the left adjacent
                elif right_adjacent.get_prime():
                    current_element.add_max_sum(left_adjacent.get_max_sum())

        # Previous layer
        layer -= 1
        first_element -= layer

    return triangle_array[0].get_max_sum()


if __name__ == '__main__':
    print(find_max_sum(read_file("input.txt")))
