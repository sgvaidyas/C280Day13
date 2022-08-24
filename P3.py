s =  "+9*26"
stk = []
for x in range(-1,-(len(s)+1),-1):
    if s[x] in "+-/*^":
        last   =  stk.pop()
        seclast = stk.pop()
        if s[x] =="^":
            stk.append(str(eval(last+"**"+seclast)))
        else:
            stk.append(str(eval(last+s[x]+seclast)))
    else:
        stk.append(s[x])
else:
    print("Value = ",stk.pop())

