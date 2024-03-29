# Defines the main function
def main():

    # Import the random module
    import random

    # Set up the briefcases with different amounts of money
    case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000,
                   100000, 200000, 300000, 400000, 500000, 750000, 1000000]

    # Randomly assign values to the cases
    random.shuffle(case_values)

    # Create a dictionary with case numbers as keys and values as amounts of money
    briefcases = {i + 1: value for i, value in enumerate(case_values)}

    # Initialize player's chosen briefcase number
    player_case_number = None

    # Initialize player's chosen briefcase value
    player_case_value = None

    # Define the rounds and the number of cases to open in each round
    rounds = [7, 5, 4, 3, 2, 1]

    # Initialize the round number
    round_number = 0

    # Start the game loop
    while True:

        # Check if the player hasn't chosen a briefcase yet
        if player_case_number is None:

            # Prompt the player to choose a briefcase
            player_case_number = int(input(f"Choose a briefcase (1-{len(briefcases)}): "))

            # Set the player's case value and remove it from the available briefcases
            player_case_value = briefcases.pop(player_case_number)

            # Announce that the player has chosen a briefcase
            print("You have chosen your briefcase. Let's start the game!")

        # Determine the number of cases to open in the current round
        if round_number < len(rounds):

            # Declaes the variable cases_to_open and assigns it to the amount of cases the contestant needs to open according to the round
            cases_to_open = rounds[round_number]

        # Else open 1 case
        else:

            # Updates the value of cases_to_open to 1
            cases_to_open = 1

        # Announce the start of the round and the number of cases to open
        print(f"Round {round_number + 1}: Open {cases_to_open} briefcases")

        # Open the specified number of briefcases
        for _ in range(cases_to_open):

            # Check if there are no more briefcases to open
            if not briefcases:

                # Break out of loop
                break

            # Display the remaining briefcases
            print(f"Remaining briefcases: {list(briefcases.keys())}")

            # Prompt the player to choose a briefcase to open
            case_number = int(input("Choose a briefcase to open: "))

            # Reveal the amount in the chosen briefcase and remove it from the available briefcases
            print(f"Briefcase {case_number} contains: ${briefcases.pop(case_number):,.2f}")

        # Make a banker's offer if there are more than one briefcase remaining
        if len(briefcases) > 1:

            # Calculate the banker's offer
            offer = sum(briefcases.values()) / len(briefcases) * random.uniform(0.8, 1.2)

            # Present the banker's offer to the player
            print(f"The banker's offer is: ${offer:,.2f}")

            # Prompt the player to accept or reject the offer
            deal = input("Deal or No Deal? (D/N): ").upper()

            # Check if the player accepts the offer
            if deal == 'D':

                # Announce the player's winnings and end the game
                print(f"Congratulations! You've won ${offer:,.2f}!")

                # Break out of loop, game over
                break

        # Make a final offer and give the option to switch cases if there is only one briefcase remaining
        if len(briefcases) == 1:

            # Calculate the final offer
            final_offer = sum(briefcases.values()) * random.uniform(0.8, 1.2)

            # Present the final offer to the player
            print(f"The banker's final offer is: ${final_offer:,.2f}")

            # Prompt the player to accept or reject the final offer
            final_deal = input("Deal or No Deal? (D/N): ").upper()

            # Check if the player accepts the final offer
            if final_deal == 'D':

                # Announce the player's winnings and end the game
                print(f"Congratulations! You've won ${final_offer:,.2f}!")

            # Else if player declines offer
            else:

                # Get the number and value of the remaining case
                remaining_case_number, remaining_case_value = briefcases.popitem()

                # Announce the remaining case
                print(f"There is only one case left: Case {remaining_case_number}")

                # Prompt the player to decide whether to switch their case with the remaining case
                switch = input("Do you want to switch your case with the remaining case? (Y/N): ").upper()

                # Check if the player chooses to switch their case
                if switch == 'Y':

                    # Announce that the player has switched their case and won the value of the remaining case
                    print(f"You have switched your case. You've won ${remaining_case_value:,.2f}!")

                # Else the player keeps their original case
                else:

                    # Announce that the player kept their original case and won its value
                    print(f"You kept your original case. You've won ${player_case_value:,.2f}!")

            # Break out of the loop, ending the game
            break

        # Announce the start of the next round
        print("Next round...\n")

        # Increment the round number to proceed to the next round
        round_number += 1

# Calls the main function to start the game
main()
