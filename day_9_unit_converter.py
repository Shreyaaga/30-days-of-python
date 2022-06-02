number=int(input('enter number in km '))
print('1-meter \n 2-centimeter \n 3-milimeter')
x=int(input('enter your choice'))

def values(x):
    info={
        1:1000,
        2:10000,
        3:100000
    }
    return info[x]

y=number*(values(x))
print(y)
if x==1:
    print('meters')
if x==2:
    print('centimeter')
if x==3:
    print('milimeter')


