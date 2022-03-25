'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 18:31:00
    @Title: main entry point of this project
'''
import logging
import sys
from functional_programs import FunctionalPrograms

file_path = r'C:\Users\Nishanth\Desktop\codingclub\CFP\Repos\Functional-Programs\FunctionalPrograms\Log files\functional_programs.log'
logging.basicConfig(handlers=[logging.FileHandler(file_path, mode="a"), logging.StreamHandler(sys.stdout)], level=logging.INFO)

FunctionalPrograms.coin_flip()