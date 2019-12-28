number = 23
running = True



while running:
    guess = int(input('Enter any integer : '))

    if guess == number:
        print ('Congratulations, you guessed it.')
        running = False
    elif guess > number:
        print ('Guessed is greater')
        running = False
    else :
        print ('chotu number --- Enter again')
        
print ("Done")


