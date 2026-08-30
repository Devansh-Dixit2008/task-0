"""
Q1. List Analyzer
Reads N integers, then computes largest, smallest, sum, even/odd counts,
and the reversed list -- all WITHOUT using max(), min(), sum(), sort(), sorted().
"""


def analyze_list(numbers):
    # Seed our "running" trackers with the first element instead of 0 or
    # infinity -- this way the function still works correctly even if every
    # number in the list is negative.
    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total += num
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Build the reversed list manually by walking the index backwards,
    # instead of using list.reverse() or list[::-1].
    reversed_list = []
    index = len(numbers) - 1
    while index >= 0:
        reversed_list.append(numbers[index])
        index -= 1

    return largest, smallest, total, even_count, odd_count, reversed_list


def main():
    n = int(input("Enter N (how many integers): "))
    raw = input(f"Enter {n} integers separated by spaces: ")
    numbers = [int(value) for value in raw.split()]

    largest, smallest, total, even_count, odd_count, reversed_list = analyze_list(numbers)

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Sum: {total}")
    print(f"Even count: {even_count}")
    print(f"Odd count: {odd_count}")
    print("Reversed:", " ".join(str(x) for x in reversed_list))


if __name__ == "__main__":
    main()
