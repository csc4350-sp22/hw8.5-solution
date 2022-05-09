def int_to_binary(n: int) -> str:
    """
    Given an integer n, convert it to binary, and return that string.
    Assumes n >= 1.
    """
    pow = 0
    while 2 ** pow < n:  # ** means exponent, for the uninitiated
        pow += 1
    if 2 ** pow > n:
        pow -= 1  # go back to the largest power that was smaller than n

    binary_string = ""
    while pow >= 0:
        if 2 ** pow <= n:
            binary_string += "1"
            n -= 2 ** pow
        else:
            binary_string += "0"
        pow -= 1

    return binary_string


def every_other_char(s: str) -> str:
    """
    Given a string, take every other character, and return the resulting
    string.

    Ex: "abc" -> "ac", "abcd" -> "ac"
    """
    every_other = ""
    for i in range(0, len(s), 2):
        every_other += s[i]

    return every_other


def refactored_function(n: int) -> int:
    """
    Honestly, who knows why this function exists?
    """
    # let's not bother with zero or negative integers
    if n <= 1:
        return 0

    binary_string = int_to_binary(n)
    every_other = every_other_char(binary_string)
    # sum up the resulting string, and return that
    res = sum(
        int(digit) for digit in every_other
    )  # this is some sneaky Python called a "comprehension" - it's basically a condensed for loop
    return res
