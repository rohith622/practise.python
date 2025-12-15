# fixed_hello.py
# Correct extraction and sorting of odd numbers from a list

def get_sorted_odds_iterative(numbers):
    result = []
    for n in numbers:
        if n % 2 != 0:
            result.append(n)
    result.sort()
    return result

def get_sorted_odds_comprehension(numbers):
    return sorted([n for n in numbers if n % 2 != 0])

def main():
    my_list1 = [3, 5, 7, 7, 8, 9, 2, 1, 4, 6]

    my_list2 = get_sorted_odds_iterative(my_list1)
    print('Odd numbers (sorted) - iterative:', my_list2)

    odd_sorted = get_sorted_odds_comprehension(my_list1)
    print('Odd numbers (sorted) - comprehension:', odd_sorted)

if __name__ == '__main__':
    main()
