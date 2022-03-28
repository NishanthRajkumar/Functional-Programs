'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 25-03-2022 19:31:00
    @Title: Functionalities for various functional programs
'''
import logging
import random

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
            if year_as_int%4 == 0 and (year_as_int%100 != 0 or year_as_int%400 == 0):
                logging.info(f"{year_as_int} is a leap year")
            else:
                logging.info(f"{year_as_int} is not a leap year")
        except ValueError:
            logging.exception("Invalid input as year")
            logging.warning("Input must be integer")