from pickle import TRUE
a=int(input('please enter number'))
b=int(input('please enter number'))
oper = input("Choose a math operation (+, -, *): ")
if oper=='+':
    x=(a+b)
elif oper=='-':
    x=(a-b)
elif oper=='*':
    x=(a*b)
elif oper=='/':
    x=(a/b) 

print(x)


