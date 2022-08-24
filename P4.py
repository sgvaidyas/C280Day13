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



def infix_postfix(s):
    global postfix
    for x in s:
        #if it is char from a-z or A-z
        if((ord(x)>=65 and ord(x)<91) or (ord(x)>=97 and ord(x)<=122)):
            postfix.append(x)
        #when we encounter ')'
        elif x=='(':
            push(x,stk)
        #operators x = + or - -->
        elif x in "+-":
            print("x = ",x)
            while peek(stk)!=None and (peek(stk) in "+-*/^"):
                ele = pop(stk)
                postfix.append(ele)
            push(x,stk)
            print("stk = ",stk)
        elif x in "*/":
            print("x",x)
            while peek(stk) in "*/^":
                ele = pop(stk)
                postfix.append(ele)
            push(x,stk)
        elif x =='^':
            push(x,stk)
        elif x==')':
            while peek(stk) !='(':
                ele = pop(stk)
                postfix.append(ele)
            pop(stk)
        print("".join(postfix))
    else:
        while(peek(stk)!=None):
            postfix.append(pop(stk))
        post = "".join(postfix)
        print("postfix expression = ",post)

stk = []
postfix = []
top=-1
#s = "(a+b-c/d)*(a^b-(c-d)/(a*b))"
#s = input("Enter the infix = ")
s = "K+L-M*N+(O^P)*W/U/V*T+Q"
max = len(s)
stk = [None]*max
postfix = []

infix_postfix(s)



