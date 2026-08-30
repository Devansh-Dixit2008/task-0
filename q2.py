"""
Q2. Lists, Functions and .copy()

Demonstrates the difference between:
    list2 = list1          # list2 is just another name for the SAME list
    list2 = list1.copy()   # list2 is an independent list with the same contents

Because we need `numbers` (the caller's original list) to stay untouched,
we operate on a .copy() of it, never on `numbers` itself.
"""


def process_list(numbers):
    # Step 1: work on a copy so the caller's original list is untouched.
    result = numbers.copy()

    # Step 2: remove all negative numbers.
    # We can't safely modify a list with .remove() while iterating over it
    # directly (that skips elements), so we loop over a separate copy of
    # `result` to decide what to remove, or equivalently rebuild the list.
    for value in numbers:  # iterate over the ORIGINAL values, not `result`
        if value < 0:
            result.remove(value)

    # Step 3: append 0.
    result.append(0)

    # Step 4: sort ascending, in place.
    result.sort()

    # Step 5: return the modified list.
    return result


def main():
    original = [5, -2, 8, -1, 3]
    result = process_list(original)
    print("Original:", original)
    print("Result:", result)


if __name__ == "__main__":
    main()
