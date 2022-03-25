'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 18:31:00
    @Title: Functionalities for various functional programs
'''
import logging

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