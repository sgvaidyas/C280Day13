def checkvowels(s,i=0):
    if (i==len(s)):
        return 0
    if s[i].lower() in "aeiou":
        return 1+checkvowels(s,i+1)
    return checkvowels(s,i+1)

s="i m so done with the session said the trainee"

print("no of vowels = ",checkvowels(s))
