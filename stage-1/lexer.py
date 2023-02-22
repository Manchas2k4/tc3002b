import os
from enum import Enum

class Tag(Enum):
	EOF = 65535
	ERROR = 65534
	## Operators ##
	GEQ = 258
	LEQ = 259
	NEQ = 260
	EQ = 261
	## REGULAR EXPRESSIONS ##
	ID = 357
	NUMBER = 358
	STRING = 359
	TRUE = 360
	FALSE = 361
	## RESERVED WORDS ##
	VAR = 457
	FORWARD = 548
	
class Token:
	__tag = Tag.EOF
	
	def __init__(self, value):
		self.__tag = value
		
	def getTag(self):
		return self.__tag
		
	def __str__(self):
		if self.__tag == Tag.GEQ:
			return "Token - value >="
		elif self.__tag == Tag.LEQ:
			return "Token - value <="
		elif self.__tag == Tag.NEQ:
			return "Token - value <>"
		elif self.__tag == Tag.EQ:
			return "Token - value :="
		elif self.__tag == Tag.TRUE:
			return "Token - value TRUE"
		elif self.__tag == Tag.FALSE:
			return "Token - value FALSE"
		elif self.__tag == Tag.VAR:
			return "Token - value VAR"
		else:
			return "TOKEN - value " + chr(self.__tag)
			
class Number(Token):
	__value = 0.0
	
	def __init__(self, val):
		super().__init__(Tag.NUMBER)
		self.__value = val

	def getTag(self):
		return super().getTag()
	
	def getValue(self):
		return self.__value
	
	def __str__(self):
		return "Number - value: " + str(self.__value)
	
class Word(Token):
	__lexeme = ""
	
	def __init__(self, tag, lex):
		super().__init__(tag)
		self.__lexeme = lex

	def getTag(self):
		return super().getTag()
	
	def getLexeme(self):
		return self.__lexeme
	
	def __str__(self):
		return "Word - lexeme: " + str(self.__lexeme)

class String(Token):
	__string = ""
	
	def __init__(self, s):
		super().__init__(Tag.STRING)
		self.__string = s

	def getTag(self):
		return super().getTag()
	
	def getString(self):
		return self.__string
	
	def __str__(self):
		return "String - text: " + str(self.__string)

class Lexer:
	__peek = ' '
	__words = {}
	__input = None

	def __init__(self, filepath):
		#assert(not(os.path.isfile(filepath)), "File Not Found")
		
		self.__input = open(filepath, "r")
		self.__peek = ' '

		self.__words["VAR"] = Word(Tag.VAR, "VAR")
		self.__words["FORWARD"] = Word(Tag.FORWARD, "FORWARD")
		self.__words["FD"] = Word(Tag.FORWARD, "FORWARD")
		## ADD ALL RESERVED WORDS ##

	def read(self):
		self.__peek = self.__input.read(1)
	
	def readch(self, c):
		self.read()
		if self.__peek != c:
			return False

		self.__peek = ' '
		return True

	def __skipSpaces(self):
		while True:
			if self.__peek == ' ' or self.__peek == '\t' or self.__peek == '\r' or self.__peek == '\n':
				self.read()
			else:
				break
	
	def scan(self):
		self.__skipSpaces()

		## ADD CODE TO SKIP COMMENTS HERE ##

		if self.__peek == '<':
			if self.readch('='):
				return Word(Tag.LEQ, "<=")
			elif self.readch('>'):
				return Word(Tag.NEQ, "<>")
			else:
				return Token(ord('<'))
		elif self.__peek == '>':
			if self.readch('='):
				return Word(Tag.GEQ, ">=")
			else:
				return Token(ord('>'))
		elif self.__peek == '#':
			if self.readch('t'):
				return Word(Tag.TRUE, "#t")
			elif self.readch('>'):
				return Word(Tag.FALSE, "#f")
			else:
				return Token(ord('#'))
		elif self.__peek == ':':
			if self.readch('='):
				#print("reading :=")
				return Word(Tag.EQ, ":=")
			else:
				return Token(ord(':'))

		if self.__peek  == '"':
			val = ""
			while True:
				val = val + self.__peek
				self.read()
				if self.__peek == '"':
					break
			
			val = val + self.__peek
			self.read()
			return String(val)

		if self.__peek.isdigit():
			val = 0
			while True:
				val = (val * 10) + int(self.__peek)
				self.read()
				if not(self.__peek.isdigit()):
					break
			## ADD CODE TO PROCESS DECIMAL PART HERE ##
			return Number(val)

		if self.__peek.isalpha():
			val = ""
			while True:
				val = val + self.__peek.lower()
				self.read()
				if not(self.__peek.isalnum()):
					break

			if val in self.__words:
				return self.__words[val]

			w = Word(Tag.ID, val)
			self.__words[val] = Word(Tag.ID, val)
			return w

		if not(self.__peek):
			return Token(Tag.EOF)			

		token = Token(ord(self.__peek))
		self.__peek = ' ' 
		return token
