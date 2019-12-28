number = puneet
guess = string(input('Enter an integer : '))


if guess == number:
    print ('Congratulations, you guessed it.')
    '''print '(but you do not win any prizes!)'''
elif guess > number :
    print ('Number is less')
else:
    print ('Guessed number is less')

print ('Done')
