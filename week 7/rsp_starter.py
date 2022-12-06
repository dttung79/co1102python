def enter_balance():
    pass
    # TODO: ask the user for their initial balance (at least $10, but no more than $100)
    # Validate input until user enters a valid balance and return it
    
def random_rsp():
    pass
    # TODO: generate a random number between 1, 2, and 3
    # return the corresponding string: "rock", "scissors" or "paper" based on the random number

def get_rsp():
    pass
    # TODO: get user input for rock, paper, or scissors.
    # Validate input until user enters a valid choice (rock, paper, or scissors) and return it

def compare_result(comp_choice, user_choice):
    pass
    # TODO: print the computer's choice and the user's choice
    # Compare user choice and computer choice folowing the rule: rock > scissors > paper > rock
    # Print the result of the game for user (win, lose, or tie)
    # Return the result of the game ('win', 'lose', or 'tie')

def is_continue():
    pass
    # TODO: ask the user if they want to play again
    # return True if the user enters "y" or "yes" and False otherwise

def update_balance(result, balance):
    pass
    # TODO: update the user's balance based on the result of the game
    # If the user wins, add $5 to their balance
    # If the user loses, subtract $5 from their balance
    # If the user ties, do not change their balance
    # Show user's new balance and return it

#### MAIN PROGRAM ####
playing = True
while playing:
    balance = enter_balance()
    comp_choice = random_rsp()
    user_choice = get_rsp()
    result = compare_result(comp_choice, user_choice)
    balance = update_balance(result, balance)
    playing = is_continue()