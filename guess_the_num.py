import random
top_of_range = 10
rn = random.randint(0, top_of_range)

print('Im thinking about a number between...')

guesses = 0

while True:
    guesses += 1
    user_input = input('guess the number: ')
    if user_input.isdigit():
        user_input = int(user_input)
    
    else:
        print('try a number next time.')
        continue
    if user_input == rn:
        print('correct:)')
        break
    elif user_input > rn:
        print('too high, try again.')
    else:
        print('too low, try again')
    if guesses >= 5:
        print(f'your ran of the guesses, you number was {rn}')
        break

if guesses > 1:
    print(f"your number of guesses: {guesses}")
else:
    print(f"your number of guess: {guesses}")

    