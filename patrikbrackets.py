import itertools

s = int(input('enter number of bracket pairs'))

def checkBalance(equation):
    push_brackets = ("(", "{", "[",)
    pop_brackets = (")", "}", "]",)
    stack = []
    balanced = 1
    for w in equation:
        if w in push_brackets:
            stack.append(w)
        if w in pop_brackets:
            if len(stack) < 1:
                balanced = 0
                break
            j = stack.pop()
            if w == ")":
                reverse = "("
            elif w == "}":
                reverse = "{"
            elif w == "]":
                reverse = "["
            if j != reverse:
                balanced = 0
                break
    if len(stack) > 0:
        balanced = 0
    if balanced == 1:
        return True
    else:
        return False
l = []
for i in range(s):
    l.append('(')
    l.append(')')
print(l)

combs = []
for item in itertools.combinations_with_replacement(l,len(l)):
    combs.append(item)


res = []
for item in combs:
    if checkBalance(item):
        res.append(item)
for i in range(len(res)):
    res[i] = ''.join(res[i])
res = set(res)
print(res)
