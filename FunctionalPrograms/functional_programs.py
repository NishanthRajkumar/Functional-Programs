'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 26-03-2022 09:19:00
    @Title: Functionalities for various functional programs
'''
from itertools import permutations
import logging
import math
import random
import sys
import time

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
    
    def coupon_generator():
        """
            Description:
                Generate N distinct coupon numbers randomly.
        """
        try:
            no_of_coupons_to_generate = input("Enter no of coupons to generate: ")
            no_of_coupons = int(no_of_coupons_to_generate)
            if no_of_coupons < 1:
                logging.warning("The no of coupons to generate must be greater 1")
                return None
            range_upper_limit = 10**(len(no_of_coupons_to_generate)+1)
            #coupons = set()
            coupons = set(random.choices(range(range_upper_limit), k=no_of_coupons))
            logging.info(f"{no_of_coupons} unique coupons: {coupons}")
        except ValueError:
            logging.exception("Invalid input for no of coupons to generate")
            logging.warning("Input must be integer")
    
    def input_2d_array():
        """
            Description:
                input integer, double and boolean values in MxN array
        """
        try:
            rows = int(input("Enter no of rows: "))
            columns = int(input("Enter no of columns: "))
            array_result = []
            for i in range(rows):
                column = []
                for j in range(columns):
                    input_value = input(f"Array[{i}][{j}]: ")
                    try:
                        final_value = int(input_value)
                    except:
                        try:
                            final_value = float(input_value)
                        except:
                            if input_value.capitalize() == "True":
                                final_value = True
                            elif input_value.capitalize() == "False":
                                final_value = False
                            else:
                                logging.error("Input to array was not int float or bool")
                                return None
                    column.append(final_value)
                array_result.append(column)
            logging.info(f"Final 2d array: {array_result}")
        except ValueError:
            logging.exception("Invalid input for rows/columns")
            logging.warning("Input must be integer")
    
    def sum_of_3ints():
        """
            Description:
                Input N integers and gets distinct triples that add to 0
        """
        try:
            no_of_int = int(input("Enter no of int to input: "))
            input_array = []
            for i in range(no_of_int):
                input_array.append(int(input(f"Array[{i}]: ")))
            distinct_triples = set()
            final_result = []
            for i in range(no_of_int-2):
                for j in range(i+1, no_of_int-1):
                    for k in range(j+1, no_of_int):
                        distinct_triples.add((input_array[i], input_array[j], input_array[k]))
            for triples in distinct_triples:
                if (triples[0]+triples[1]+triples[2]) == 0:
                    final_result.append(triples)
            logging.info(f"triples that sum to 0: {final_result}")
        except ValueError:
            logging.error("Input must be integer")
    
    def distance():
        """
            Description:
                Gets x and y from cmd line arguments.
                Computes distance between (x,y) and (0,0)
        """
        if len(sys.argv) < 3:
            logging.error("invalid no of cmd line arguments")
            return None
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            distance = math.sqrt((x**2)+(y**2))
            logging.info(f"Distance of ({x},{y}) from (0,0): {distance}")
        except ValueError:
            logging.error("Cmd argument passed must be integer")
    
    def string_permutation():
        """
            Description:
                finds all permutation of 2 strings and checks if the resulting arrays are equal
        """
        string1 = input("Enter 1st string: ")
        string2 = input("Enter 2nd string: ")
        if len(string1) != len(string2):
            logging.info("The permutations of the 2 strings ({string1}, {string2}) are not equal")
            return None
        string1_set = set()
        string2_set = set()
        for permutation in permutations(string1):
            string1_set.add("".join(permutation))
        for permutation in permutations(string2):
            string2_set.add("".join(permutation))
        difference  = string1_set - string2_set
        if len(difference) == 0:
            logging.info(f"The permutations of the 2 strings ({string1}, {string2}) are equal")
        else:
            logging.info(f"The permutations of the 2 strings ({string1}, {string2}) are not equal")
    
    def stopwatch():
        """
            Description:
                Simulate stopwatch program
        """
        start = time.time()
        input("StopWatch started! Hit enter to stop: ")
        end = time.time()
        logging.info(f"Stopwatch ran for {end-start}")