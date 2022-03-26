'''
    @Author: Nishanth
    @Date: 25-03-2022 18:31:00
    @Last Modified by: Nishanth
    @Last Modified time: 26-03-2022 12:55:00
    @Title: main entry point of this project
'''
import logging
import sys
from functional_programs import FunctionalPrograms

file_path = r'Log files\functional_programs.log'
logging.basicConfig(handlers=[logging.FileHandler(file_path, mode="a"), logging.StreamHandler(sys.stdout)], level=logging.INFO)

FunctionalPrograms.quadratic_eq()