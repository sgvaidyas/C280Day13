def count_digits(number):
    if number:
        return count_digits(number//10) + 1
    else:
        return 0


print(count_digits(88765))
