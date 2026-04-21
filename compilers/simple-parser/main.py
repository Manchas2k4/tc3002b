from Lexer import *
from Parser import *
import sys

if __name__ == '__main__':
    parser = Parser("test_cases/bad/input04.txt")
    parser.analize()