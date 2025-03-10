from enum import IntEnum

class Tag(IntEnum):
	EOF = 65535
	ERROR = 65534
	## Operators ##
	GEQ = 258
	LEQ = 259
	NEQ = 260
	ASSIGN = 261
	## REGULAR EXPRESSIONS ##
	ID = 358
	NUMBER = 359
	STRING = 360
	TRUE = 361
	FALSE = 362
	## ADD THE MISSING RESERVED WORDS, JUST FOLLOW THE NUMBER SEQUENCE ##
	VAR = 457
	FORWARD = 458
	
class Token:
	tag = Tag.EOF
	value = None
	
	def __init__(self, tagId, val = None):
		self.tag = tagId
		self.value = val
		
	def __str__(self):
		if self.tag == Tag.GEQ:
			return "'>='"
		elif self.tag == Tag.LEQ:
			return "'<='"
		elif self.tag == Tag.NEQ:
			return "'<>'"
		elif self.tag == Tag.ASSIGN:
			return "':='"
		elif self.tag == Tag.TRUE:
			return "'#T'"
		elif self.tag == Tag.FALSE:
			return "'#F'"
		elif self.tag == Tag.NUMBER:
			return str(self.value)
		elif self.tag == Tag.ID:
			return "'" + str(self.value) + "'"
		elif self.tag >= Tag.VAR and self.tag <= Tag.MOD:
			return "'" +  str(self.value) + "'"
		elif self.tag == Tag.STRING:
			return str(self.value)
		else:
			return "'" + chr(self.tag) + "'" 
			
class Lexer:
	file_path = None
	position = 0
	buffer_size = 0
	current_path = None
	next_buffer = None
	words = {}

	def __init__(self, file_path, buffer_size = 1014):
		self.file_path = file_path
		self.buffer_size = buffer_size
		self.position = 0
		self.current_path = ""
		self.next_buffer = ""

		with open(self.file_path, 'r') as file:
			file.seek(self.position)
			self.current_buffer = file.read(self.buffer_size)
			self.next_buffer = file.read(self.buffer_size)
			self.position += self.buffer_size

		self.__words["VAR"] = Token(Tag.VAR, "VAR")
		self.__words["FORWARD"] = Token(Tag.FORWARD, "FORWARD")
		self.__words["FD"] = Token(Tag.FORWARD, "FORWARD")
		## ADD THE REST RESERVED WORDS, REMEMBER THAT SOME RESERVER WORDS HAVE THE SAME TAG ##

	def get_next_character(self):
		if len(self.current_buffer) == 0 and len(self.next_buffer) > 0:
			self.current_buffer = self.next_buffer
			with open(self.file_path, 'r') as file:
				file.seek(self.position)
				self.next_buffer = file.read(self.buffer_size)
				self.position += self.buffer_size

		if len(self.current_buffer) > 0:
			character = self.current_buffer[0]
			self.current_buffer = self.current_buffer[1:]
			return character
		
		return None
	
	def push_back(self, character):
		self.current_buffer = character + self.current_buffer

	def scan(self):
		while True:
			character = self.get_next_character()

			if character is None:
				return Token(Tag.EOF)
			
			if character.isspace():
				continue

			if character == '%':
				while True:
					character = self.get_next_character()
					if character == '\n':
						break
				continue

			if character == '<':
				character = self.get_next_character()
				if character in ['=', '>']:
					if character == '=':
						return Token(Tag.LEQ, "<=")
					else:
						return Token(Tag.NEQ, "<>")
				else:
					self.push_back(character)
					return Token(ord('<'))
				
			if character == '>':
				character = self.get_next_character()
				if character == '=':
					return Token(Tag.GEQ, ">=")
				else:
					self.push_back(character)
					return Token(ord('>'))
				
			if character == '#':
				# ADD CODE TO SKIP COMMENTS HERE #
				pass
				
			if character == ':':
				character = self.get_next_character()
				if character == '=':
					return Token(Tag.ASSIGN, ":=")
				else:
					self.push_back(character)
					return Token(ord(':'))
				
			if character == '"':
				text = ""
				while True:
					text += character
					character = self.get_next_character()
					if character == '"':
						break
				text += character
				return Token(Tag.STRING, text)
			
			if character.isdigit():
				value = 0.0
				while True:
					value = (value * 10) + int(character)
					character = self.get_next_character()
					if not character.isdigit():
						break
				## ADD CODE TO PROCESS DECIMAL PART HERE ##
				self.push_back(character)
				return Token(Tag.NUMBER, value)
			
			if character.isalpha():
				lexem = ""
				while True:
					lexem += character.upper()
					character = self.get_next_character()
					if not character.isalnum():
						break
				self.push_back(character)

				if lexem in self.words:
					return self.words[lexem]
				
				token = Token(Tag.ID, lexem)
				self.words[lexem] = token
				return token
			
			return Token(ord(character))