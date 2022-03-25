'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 18:31:00
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