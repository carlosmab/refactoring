def fizzbuzz(number):
    result = ""
    result += divisible_by_n(number, 3, "Fizz")
    result += divisible_by_n(number, 5, "Buzz")
    return result or str(number)


def divisible_by_n(number, n, word):
    return word if number % n == 0 else ""

