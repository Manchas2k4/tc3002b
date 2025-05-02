"""
=========================================================
File: Lexer.py
Author: Pedro Pérez, Miguel Weiping Tang Feng
Date: 10/abril/2022
=========================================================
"""
from Lexer import *
from Parser import *
import sys

if __name__ == '__main__':
	print("----GOOD TEST CASES----")
	for i in range(7):
		parser = Parser(f"test_cases/good/prog{i + 1}.txt")
		parser.analize()
		print(f"Test #{i + 1}: END")
	
	print("----BAD TEST CASES----")
	for i in range(7):
		try:
			parser = Parser(f"test_cases/bad/prog{i + 1}.txt")
			parser.analize()
			print(f"Test #{i + 1} Passed <-- Shouln't pass")
		except Exception as e:
			print(f"Test #{i + 1} failed: {e}")
