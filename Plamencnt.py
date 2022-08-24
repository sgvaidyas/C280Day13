num = 123456789
a = 1
def count(num):
    global a
    if num < 10:
        return a
    a = 1 + count(num/10)
    return a
print(count(num))
