import random

from traitlets import Int
greeting=[]
intro=[]
sentence=[]

greeting.append('hope i have found u in your best spirit ')
greeting.append('hope u and your owrk is going great ')
greeting.append('i like u and i am amaezed i am talking to you' )
intro.append('heyy!! ')
intro.append('hiihhihihihihi!! ')
intro.append('whatsss upp!! ')
sentence.append('Im going to teach you how to become a software engineer')
sentence.append('I will show you how to actually learn engineering skills.')
sentence.append('If you want to truly learn Python in a useable manner, you should follow me')

full_greeting=random.choice(intro)+random.choice(greeting)+random.choice(sentence)
print('-----------------------------------------------------------------------------------------------------')
print(full_greeting)
print('------------------------------------------------------------------------------------------------------')