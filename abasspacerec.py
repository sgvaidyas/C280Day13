def printme(s, cnt, l):
    l += 1
    if l == len(s):
        return print(f"The number of words are: {cnt+1}")
    char = s[l]
    char2 = s[l-1]
    check = True
    for i in range(l,len(s)):
        if s[i].isalpha():
            check = False
    if char == " " and char2.isalpha() and check == False:
        printme(s, cnt + 1, l)
        s.replace(char,"")
    else:
        printme(s, cnt, l)
s = input("Enter text: ")
printme(s, 0, -1)
