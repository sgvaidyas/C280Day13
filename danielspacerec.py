def recursive_space_equilazerrr(s, i=0):
    while i < len(s)-1:
        if s[i] == " " and s[i - 1] == " ":
            return recursive_space_equilazerrr(s, i + 1)
        else:
            return str(s[i]) + str(recursive_space_equilazerrr(s, i + 1))
    return ""

s = "         if you are happy       that u got the job    .....  i appreciate your innocence    "
print(recursive_space_equilazerrr(s))
