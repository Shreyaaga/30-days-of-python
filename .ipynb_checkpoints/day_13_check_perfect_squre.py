from cmath import sqrt
import math
from traceback import print_tb
user_number=int(input('enter a number if u want to know that is it a perfect square'))
after_sqrt=math.sqrt(user_number)
if (after_sqrt-int(after_sqrt))==0:
    print('square root of {} is {}'.format(user_number,after_sqrt))
else:
    print('No it is not a perfect square')