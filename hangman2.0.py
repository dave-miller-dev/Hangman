import random
something = ''


def end():
    if "-" not in something:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")


def main():
    print("H A N G M A N")
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "play":
        ok_guesses = ['python', 'java', 'kotlin', 'javascript']
        selected = random.choice(ok_guesses)
        something = selected
        guess_count = 0
        guess_set = []
        for _ in something:
            something = something.replace(_, "-")
        while guess_count < 8:
            print("")
            print(something)
            guess = input("Input a letter:")
            if len(guess) != 1:
                print("You should input a single letter")
            else:
                if guess.islower():
                    if guess in selected:
                        if guess in guess_set:
                            print("You already typed this letter")
                        else:
                            x = selected.find(guess)
                            temp = list(something)
                            temp[x] = guess
                            something = "".join(temp)
                    else:
                        if guess in guess_set:
                            print("You already typed this letter")
                        else:
                            print("No such letter in the word")
                            guess_count = guess_count + 1
                    guess_set.append(guess)
                else:
                    print("It is not an ASCII lowercase letter")
        end()
    elif choice == "exit":
        pass


main()
