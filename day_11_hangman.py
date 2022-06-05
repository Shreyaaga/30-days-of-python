import random
words=['act', 'air', 'age', 'bag', 'cap', 'map', 'area', 'baby', 'card', 'dish', 'exam', 'good', 'boards', 'chair', 'count', 'facts', 'green', 'house']
index=random.randint(0,17)
word_choosed=words[index]


hangman_graphics = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '                
                    ]


no_of_mistakes=0
no_mistakes_allowed=len(hangman_graphics)
wrong_letter_guessed=[]
letters_correctly_guessed=[]

print()                       #to print single blank line
print('the word has {} letters'.format(len(word_choosed)))    #to tel the user how many letters are there in the word to be guessed

while no_of_mistakes<no_mistakes_allowed:
    print('wrong guesses-',end='')
    for letter in wrong_letter_guessed:
        print("{}".format(letter),end=' ')
    print()
    print("guesses left {}".format(no_mistakes_allowed-no_of_mistakes))
    user_input=input('guess a letter:')


    while user_input in letters_correctly_guessed or user_input in wrong_letter_guessed:
        print('you have entrted invalid letter which is already been entered')
        user_input=input('guess a letter:')

    if user_input not in word_choosed:
            no_of_mistakes += 1
            wrong_letter_guessed.append(user_input)


    #printing the letter with blanks(_) also
    print('word-',end='')
    for letter in word_choosed:
        if letter ==user_input:
            letters_correctly_guessed.append(user_input)
            
        
    for letter in word_choosed:
        if letter in letters_correctly_guessed:
            print(letter," ",end='')
        else:
            print('_'," ",end='')
    #creating hanagman
    print()
    print("hangman status")
    if no_of_mistakes:
        print(hangman_graphics[no_of_mistakes - 1])
    print()
    print('-------------------------------------------')
    
    if len(letters_correctly_guessed) == len(word_choosed):
        print()
        print('YOU WOOOON!!!')
        break

if no_of_mistakes == no_mistakes_allowed:
    print()
    print('YOU LOST! TRY AGAIN!')   
