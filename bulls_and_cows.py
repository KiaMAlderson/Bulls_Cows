def bulls_cows():
    line_1 = ""
    line_2 = ""
    secret = ""
    guesses = []
    num_guess = 0
    len_line_2 = 0
    to_append = ""
    
    print("------------------------------------")
    line_1 = input("Enter the secret value, a space, then the number of guesses: ")

    if (line_1[4] != ' '):
        raise Exception("INPUT LINE 1 SPACE ERROR")
    secret = line_1[0:4]
    num_guess = int(line_1[5:])

    print("------------------------------------")
    line_2 = input("Enter the guesses: ")
    print("------------------------------------")
    len_line_2 = len(line_2)

    if (((len_line_2 + 1)/5) != num_guess):
       raise Exception("INCORRECT NUMBER OF GUESSES ENTERED ERROR")

    for i in range(0, num_guess):
        try:
            if((line_2[((i+1)*5)-1]) != ' '):
                raise Exception("INPUT LINE 2 SPACE ERROR")
        except IndexError:
            pass

        try:
            to_append = line_2[(i*5):(((i+1)*5)-1)]
            guesses.append(to_append)
        except IndexError:
            to_append = line_2[(i*5):]
            guesses.append(to_append)

    print("Answer:")
    answer = ""
    for guess in guesses:
        answer += check_guess(secret, guess, num_guess)
    print(answer)

def check_guess(secret, guess, num_guess):
    correct_place = 0
    wrong_place = 0
    length_secret = len(secret)
    
    for i in range(0, length_secret):
        if (guess[i] == secret[i]):
            correct_place += 1

        for j in range(0, len(secret)):
            if((guess[j] == secret[i]) & (i == j)):
                continue
            elif(guess[j] == secret[i]):
                wrong_place += 1
            else:
                continue
    returner = str(correct_place) + "-" + str(wrong_place) + " "
    
    return(returner)

bulls_cows()
