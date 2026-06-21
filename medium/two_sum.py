from utils import input_util


def two_sum(numbers, sum_to_be_found):
    """
    Returns the indices of the target value in the array that add upto given sum if found, otherwise -1.

    Args:
        numbers: A list of integers to search in.
        sum_to_be_found: An integer representing the sum of 2 elements in numbers.

    Returns:
        List of the indices of the 2 target values in the list that add upto sum, otherwise empty list.

    Example:
        Input: numbers = [10,20,30,40], sum_to_be_found = 50
        Output: [[0,3], [1,2], [2,1], [3,0]]

    """
    target_indices = []
    for i  in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum_to_be_found:
                target_indices.append([i, j])
    return target_indices


def main():
    numbers = input_util.get_list_of_integers_from_input()
    sum_to_be_found = input_util.get_positive_integer_from_input("Sum to be found")
    final_list= two_sum(numbers, sum_to_be_found)
    print(final_list)

if __name__ == '__main__':
    main()