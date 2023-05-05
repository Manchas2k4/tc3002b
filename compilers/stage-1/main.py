from lexer import *
import sys

if __name__ == '__main__':
	lexer = Lexer("test_cases/prog1.txt")
	
	token = lexer.scan()
	while token.getTag() != Tag.EOF:
		print(str(token))
		token = lexer.scan()
	print("END")
