import random

highest = 10
answer = random.randint(0, highest)

print('welcome to the guessing game! I/m thinking about a number between 0 and 10...')
score = 0
while True:
    user_input = input('type your guess here: ')
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print('please enter a number next time.')
        continue
    if user_input == answer:
        print('correct!')
        score += 1
        break
    elif user_input > answer:
        print('too high, try a lower number next time.')
    else:
        print('too low, try a higher number next time.')
    if score >= 4:
        print(f'your ran out of the guesses, the number was {answer}')
        break
print(f'your answer is {answer}')

while True:
    play_again = input('do you want to play again? (yes/no): ')
    if play_again.lower() == 'yes':
        highest = 50
        answer = random.randint(0, highest)
        print('Now you are in a harder level. I/m thinking about a number between 0 and 50...')
        score = 0
        while True:
            user_input = input('type your guess here: ')
            if user_input.isdigit():
                user_input = int(user_input)
            else:
                print('please enter a number next time.')
                continue
            if user_input == answer:
                print('correct!')
                score += 1
                break
            elif user_input > answer:
                print('too high, try a lower number next time.')
            else:
                print('too low, try a higher number next time.')
            if score >= 25:
                print(f'your ran out of the guesses, the number was {answer}')
                break
    elif play_again.lower() == 'no':
        print('good bye:(')
        break
    
        
      

quit()



