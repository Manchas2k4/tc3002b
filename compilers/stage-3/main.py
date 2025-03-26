from Lexer import *
from Parser import *
from Translator import *
import sys

if __name__ == '__main__':
	parser = Parser("test_cases/good/prog1.txt")
	tree = parser.analize()

	if tree != None:
		tree.eval()
