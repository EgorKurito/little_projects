import random

# главная функция игры
def game():
    # генерация случайного числа от 1 до 10
    secret_num = random.randint(1, 10)

    # Список чисел пользователя
    guesses = []

    while len(guesses) < 3:
        # проверка того, что пользователь ввел число
        try:
            # считывание числа пользователя
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # проверка числа пользователя
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess > secret_num:
                print("Your number is too high")
            else:
                print("Your number is too low")
            guesses.append(guess)
    else:
        print("You didnt get it. My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
