'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 25-03-2022 21:29:00
    @Title: Functionalities for various functional programs
'''
import logging
import random
import sys

class FunctionalPrograms:

    def greeting():
        """
            Description:
                Greets the user based on the username entered by the user
        """
        while True:
            username = input("Enter User name: ")
            if len(username) < 3:
                logging.warning(f"user_input: {username}; User name must be min 3 characters")
                continue
            logging.info(f"Hello {username}, how are you?")
            break
    
    def coin_flip():
        """
            Description:
                Computes the percentage of Heads and Tails in n number of flips.
                value of n is entered by user
        """
        try:
            no_of_flips = int(input("Enter total no of times to flip: "))
            no_of_heads = 0
            no_of_tails = 0
            for _ in range(no_of_flips):
                result = random.random()
                if result < 0.5:
                    no_of_tails += 1
                    continue
                no_of_heads += 1
            head_percentage = no_of_heads/no_of_flips*100
            tail_percentage = no_of_tails/no_of_flips*100
            logging.info(f"Percentage of head: {head_percentage}%; Percentage of tail: {tail_percentage}")
        except ValueError:
            logging.exception("Invalid input to no of flips")
            logging.warning("Input must be integer")
    
    def leap_year():
        """
            Description:
                checks if year entered by the user is a leap year or not
        """
        try:
            while True:
                year = input("Enter year(4 digit no only): ")
                if len(year) != 4:
                    logging.warning(f"user_input: {year}; year must be 4 digits")
                    continue
                year_as_int = int(year)
                break
            if year_as_int%4 == 0:
                logging.info(f"{year_as_int} is a leap year")
            else:
                logging.info(f"{year_as_int} is not a leap year")
        except ValueError:
            logging.exception("Invalid input as year")
            logging.warning("Input must be integer")
    
    def power_of_2():
        """
            Description:
                Takes a command-line argument N.
                Prints a table of the powers of 2 that are less than or equal to 2^N.
        """
        try:
            table_limit = int(sys.argv[1])
            for i in range(table_limit):
                logging.info(f"2^{i} = {2**i}")
        except ValueError:
            logging.exception("Invalid command line Argument")
            logging.warning("Command line argument after name of python file must be integer")
        except IndexError:
            logging.exception("Command line argument not found")
            logging.warning("Command line argument must be passed")
    
    def harmonic_no():
        """
            Description:
                Computes the Nth harmonic number.
                N is obtained from user
        """
        try:
            user_input = int(input("Enter a number: "))
            def harmonic_no(number):
                if number == 1:
                    return 1
                if number > 1:
                    return (1/number)+harmonic_no(number-1)
                if number < 1:
                    logging.warning("input number must be greater than 0")
                    return 0
            result = harmonic_no(user_input)
            logging.info(f"Harmonic no of {user_input} is {result}")
        except ValueError:
            logging.exception("Invalid input for number")
            logging.warning("Input must be integer")
    
    def prime_factors():
        """
            Description:
                Computes the prime factorization of N.
        """
        try:
            user_input = int(input("Enter a number greater than 2: "))
            if user_input <= 2:
                logging.warning("Input number must be greater than 2")
                return None
            def prime(number):
                if number >= 1 and number <= 3:
                    return True
                for i in range(2, int(number/2)):
                    if number%i == 0:
                        return False
                return True
            prime_factor_list = []
            for i in range(1, user_input+1):
                if prime(i) and user_input%i == 0:
                    prime_factor_list.append(i)
            logging.info(f"Prime factors of {user_input}: {prime_factor_list}")
        except ValueError:
            logging.exception("Invalid input for number")
            logging.warning("Input must be integer")
    
    def gambler():
        """
            Description:
                Simulates a gambler who start with $stake and place fair $1 bets until goes broke or reach $goal. 
                Keeps track of the number of wins and the number of bets.
        """
        bets_dict = {}
        no_of_wins = 0
        total_no_bets = 0
        stake = int(input("Enter stake($): "))
        goal = int(input("Enter goal($): "))
        repeat_no = int(input("Enter no of times to repeat: "))
        if stake < 1 or goal < 1 or repeat_no < 1:
            logging.warning("Input no must be greater than 1")
            return None
        if stake > goal:
            logging.warning("Goal must be greater than stake")
            return None
        for i in range(1, repeat_no+1):
            cash_in_hand = stake
            game_bets_total = 0
            while True:
                gamble_sucess = random.choice([0,1])
                game_bets_total += 1
                if gamble_sucess:
                    cash_in_hand += 1
                else:
                    cash_in_hand -= 1
                if cash_in_hand == goal:
                    no_of_wins += 1
                    total_no_bets += game_bets_total
                    bets_dict[f"Game {i}"] = (game_bets_total, 'won')
                    break
                if cash_in_hand == 0:
                    total_no_bets += game_bets_total
                    bets_dict[f"Game {i}"] = (game_bets_total, 'lost')
                    break
        average_bets_per_game = total_no_bets/repeat_no
        win_percentage = no_of_wins/repeat_no*100
        logging.info(f"No of games: {repeat_no}; average bets: {average_bets_per_game}; win_percentage: {win_percentage}\n Game bets details: {bets_dict}")
                