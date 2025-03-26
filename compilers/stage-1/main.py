from Lexer import *
import sys

if __name__ == '__main__':
	lexer = Lexer("test_cases/bad/prog1.txt")
	
	token = lexer.scan()
	while token.tag != Tag.EOF:
		print(str(token))
		token = lexer.scan()
	print("END")