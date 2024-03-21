""" Main functions to run the game """

import string, random

commands = ['/help', '/vowels', '/caps', '/middle', '/end', '/common', '/all_info', '/quit', '/answer']
vowels = ['a', 'e', 'i', 'o', 'u']

def start(testing = False, test_password = ""):
    """
    This sets up the game, having the user set a password length.
    Then, a random string of uppercase and lowercase letters are generated.
    Finaly, the user must attempt to guess this password by using various commands.
    
    Parameters
    ----------
    
    None
    
    Returns
    ----------
    Nothing
    
    """
    # If testing, then set a custom password
    if testing:
        setup(len(test_password), test_password)
        return
    
    # Wait for an input that is an integer
    
    difficulty = input("Enter Password Length: ")
    while type(difficulty) != int:
        try:
            difficulty = int(difficulty)
        except:
            print("Must be an integer!")
            difficulty = input("Enter Password Length: ")
            continue
            
    # Starts the main game
    setup(difficulty)
    pw_guess()

def setup(pw_length, set_password = ""):
    """
    This function generates the password along with information about it.
    This information includes:
    - number of upper case letters
    - a dictionary to display the number of each vowel
    - the middle most letter(s)
    - the first and last letter
    - the most common letter
    
    Parameters
    ----------
    pw_length:
        integer: the length of the password set by the user
    
    Returns
    -------
    Nothing
    
    """
    
    global pw
    
    # Set a password if testing
    
    if set_password != "":
        pw = set_password
        upper_case_count()
        vowels_in_pw()
        middle()
        end_points()
        common()
        return
    
    # Generates the password
    
    pw = ""
    while True:
        if len(pw) == pw_length:
            break
        pw += random.choice(string.ascii_letters)
        
    # Generate information about the password
    
    upper_case_count()
    vowels_in_pw()
    middle()
    end_points()
    common()
    
    return

def execute_command(command):
    """
    This function takes the input command from the player
    and checks which command to execute
    
    Parameters
    ----------
    command:
        string: a string found in the commands list
        
    Returns
    ----------
    Prints information on the password based on the command entered
    
    """ 
    
    # Lists all commands
    
    if command == commands[0]:
        for prompt in commands:
            print(prompt)
        return 
    
    # Number of each vowel
    
    if command == commands[1]:
        print(vowels_count)
        return
    
    # Number of capitalized letters 
    
    if command == commands[2]:
        print(upper_count)
        return
    
    # Gives the middle most letter(s)
    
    if command == commands[3]:
        print(mid_letter)
        return
    
    # Gives the first and last letter of the password
    
    if command == commands[4]:
        print(end_points)
        return
    
    # Most Common Letter in password
    
    if command == commands[5]:
        print(most_frequent)
        return
    
    # Gives information of all the commands above (except help)
    
    if command == commands[6]:
        print("Vowel info: " + str(vowels_count))
        print("Number of upper case letters: " + str(upper_count))
        print("The middle most letter(s): " + str(mid_letter))
        print("The first and last letters: " + str(ending_letters))
        print("The most common letter: " + str(most_frequent))
        return
    
    # Gives the password
    
    if command == commands[-1]:
        print(pw)
        return

def check_guess(guess):
    """
    Checks each character in the users guess and displays information
    so the user can make a better guess.
    
    Parameters
    ----------
    guess: 
        string: This is the users input, will not be the correct answer
        
    Returns
    ----------
    guess_information:
        String: 
    Prints infromation about the letters in the users input:
    - the letter if it is correct
    - "*" if the correct letter but wrong spot
    - "^" if the letter needs to be upper/lower case
    - "~" if letter not found in password
    - "_" if the users guess is not as long as the password (each letter not guessed)
    
    """
    
    guess_information = ""
    
    # Returns if the guess length is larger than the passwords length
    
    if len(guess) > len(pw):
        guess_information = "Guess with less letters!"
        return guess_information
    
    # Checks what parts of the players guess are correct, partially correct, or wrong
    
    guess = list(guess)
    correct_guess = []
    for index, letter in enumerate(guess):
        
        # If correct
        
        if letter == pw[index]:
            correct_guess.append(letter)
            continue
            
        # If the correct letter, but in the wrong spot
        
        if letter in pw:
            correct_guess.append('*')
            continue
        
        # If the correct letter, but not capitalized/lowercase
        
        if letter.lower() in pw.lower():
            correct_guess.append('^')
            continue
        
        # Letter is wrong
        
        correct_guess.append("~")
    
    # Prints "_" for each letter that was not guessed
    
    if len(guess) < len(pw):
        for i in range(len(pw) - len(guess)):
            correct_guess.append("_")
    
    # Returns the feedback
    
    guess_information = "".join(correct_guess)
    return guess_information

def upper_case_count():
    """
    Counts the number of upper case letters
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    upper_count:
        integer: number of upper case letters
    
    """
    
    # Finds the number of Capitalized letters in the password
    
    global upper_count
    upper_count = 0
    for letter in pw:
        if letter.isupper():
            upper_count += 1
            
    return upper_count

def vowels_in_pw():
    """
    Creates a dictionary to show the number of each vowel in the password
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    vowels_count:
        dictionary: a dictionary with a vowel as a key to a number,
                    which represents the amount of that letter in the password
    
    """
    
    # Finds the number of each vowel in the password
    
    global vowels_count
    vowels_count = {}
    for letter in vowels:
        pw_list = list(pw.lower())
        letter_count = pw_list.count(letter)
        vowels_count[letter] = letter_count  
    return vowels_count

def middle():
    """
    Displays the middle most letter if the password is an odd length,
    or the middle two letters if the password is an even length
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    mid_letter:
        If the password is an odd number of characters, a single character string
        If the password is an even number of characters, a list of 2 strings
    
    """

    global mid_letter
    pw_list = list(pw)
    
    # When list has an odd number
    
    if len(pw_list) % 2 == 1:
        mid_point = int((len(pw_list) - 1) / 2)
        mid_letter = pw_list[mid_point]
        return mid_letter
    
    # When list has an even number
    
    mid_points = int((len(pw_list) - 2) / 2)
    mid_letter = [
        pw_list[mid_points],
        pw_list[mid_points + 1]
    ]
    return mid_letter

def end_points():
    """
    Displays the last letter and the first letter in the password
    If the password is 1 character long, then it will display that character
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    ending_letters:
        If the password length is 1 letter, a single character string
        Otherwise, a list with two single character strings
    
    """
    
    # Finds the first and last letter in the password
    
    global ending_letters
    # Checks if password is 1 character
    if len(pw) == 1:
        ending_letters = list(pw)
        return ending_letters
    
    # Gives the first and last letter of the password
    
    ending_letters = [
        pw[0],
        pw[-1]
    ]
    return ending_letters

def common():
    """
    Finds the most common letter in the password
    If there is are multiple characters that share the same frequecy,
    it will return the first of the letters
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    most_frequent:
        String: A single character string
    
    """
    
    global most_frequent
    
    # Generates frequency of letters
    
    letter_frequency = {}
    pw_list = list(pw)
    for letter in pw:
        letter_count = pw_list.count(letter)
        letter_frequency[letter] = letter_count
    
    # Finds the most common letter
    
    max_frequency = 0
    for letter in letter_frequency:
        if letter_frequency[letter] > max_frequency:
            max_frequency = letter_frequency[letter]
    
    letter_keys = list(letter_frequency.keys())
    frequency = list(letter_frequency.values()).index(max_frequency)
    
    most_frequent = letter_keys[frequency]
    
    return most_frequent
    
def pw_guess():
    """
    The main function that runs the game.
    Keeps running until the users input is the password,
    or the user types '/quit'.
    
    At the end it will display the number of guesses the player took
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    Either prints a single string if the player types '/quit',
    or prints a single string with the number of attempts to guess the password
    
    """
    
    num_attempts = 0
    player_inp = ""
    print("\nType '/help' to see commands")
    print("\n'~' = Wrong letter\n'*' = Correct letter but wrong spot")
    print("'^' = Correct letter but wrong punctuation\n'_' = Did not guess")
    
    # While the players guess is not the password
    
    while player_inp != pw:
        
        # Voids the firs loop and any blank guesses
        
        if player_inp == "":
            player_inp = input("\nEnter guess: ")
            continue
            
        # If the player wants to quit, then quit
        
        if player_inp == '/quit':
            print("\nThanks for playing!")
            return
        
        # If the player types a command, execute the command
        
        if player_inp in commands:
            execute_command(player_inp)
        
        # Otherwise, check the players guess to give feedback to the player
        
        else:
            num_attempts += 1
            print(check_guess(player_inp))
        
        # Asks the player for their next guess
        
        player_inp = input("\nEnter guess: ")
    
    # Displays vicotry message and provides the number of attempts
    
    victory_string = str("\nVictory!\nIt took you: " + str(num_attempts + 1) + " attempts!")
    print(victory_string)
    return
