def push(ele,l):
    global top
    if top==max-1:
        return None
    else:
        top+=1
        l[top]=ele


def pop(l):
    global top
    if top==-1:
        return None
    else:
        top-=1
        return l[top+1]

def peek(l):
    if top==-1:
        return None
    else:
        return l[top]



def infix_prefix(s):
    global prefix
    for x in s:
        #if it is char from a-z or A-z
        if((ord(x)>=65 and ord(x)<91) or (ord(x)>=97 and ord(x)<=122)):
            prefix.append(x)
        #when we encounter ')'
        elif x==')':
            push(x,stk)
        #operators x = + or - -->
        elif x in "+-":
            while peek(stk)!=None and (peek(stk) in "*/^"):
                ele = pop(stk)
                prefix.append(ele)
            push(x,stk)
        elif x in "*/":
            while peek(stk) == "^":
                ele = pop(stk)
                prefix.append(ele)
            push(x,stk)
        elif x =='^':
            push(x,stk)
        elif x=='(':
            while peek(stk) !=')':
                ele = pop(stk)
                prefix.append(ele)
            pop(stk)
        print(prefix)
    else:
        while(peek(stk)!=None):
            prefix.append(pop(stk))
        pre = "".join(prefix)
        prefix=pre[::-1]
        print("Prefix expression = ",prefix)
stk = []
prefix = []
top=-1
#s = "(a+b-c/d)*(a^b-(c-d)/(a*b))"
s = input("Enter the infix = ")
max = len(s)
stk = [None]*max
prefix = []
s = s[::-1]

infix_prefix(s)



