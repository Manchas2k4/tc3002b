from Lexer import *

class Parser:
	__lex = None
	__token = None

	def __init__(self, filepath):
		self.__lex = Lexer(filepath)
		self.__token = None

		""" DEFINE FIRST SET """
		self.__firstE = self.__firstT = self.__firstF = set((Tag.ID, ord('(')))
		self.__firstEPrime = set((ord('+'), ord('-')))
		self.__firstTPrime = set((ord('*'), ord('/')))

	def __error(self, extra = None):
		text = 'Line ' + str(self.__lex.getLine()) + " - " 
		if extra == None:
			text = text + "."
		else:
			text = text + extra
		raise Exception(text)

	def __check(self, tag):
		if self.__token.getTag() == tag:
			self.__token = self.__lex.scan()
		else:
			text = 'Line ' + str(self.__lex.getLine()) + " - expected "
			if tag != Tag.ID:
				print("tag = ", tag)
				text = text + str(Token(tag)) + " before " + str(self.__token) 
			else:
				text = text + "an identifier before " + str(self.__token) 
			self.__error(text)
	
	def analize(self):
		self.__token = self.__lex.scan()
		self.__E()
		if self.__token.getTag() == Tag.EOF:
			print("ACCEPTED")

	""" IMPLEMENT PRODUCTIONS """
	def __E(self):
		if self.__token.getTag() in self.__firstE:
			self.__T()
			self.__EPrime()
		else:
			self.__error("Wating E")
	
	def __T(self):
		if self.__token.getTag() in self.__firstT:
			self.__F()
			self.__TPrime()
		else:
			self.__error("Waiting for T")

	def __F(self):
		if self.__token.getTag() in self.__firstF:
			if self.__token.getTag() == Tag.ID:
				self.__check(Tag.ID)
			elif self.__token.getTag() == ord('('):
				self.__check(ord('('))
				self.__E()
				self.__check(ord(')'))
		else:
			self.__error("Waiting for F")

	def __EPrime(self):
		if self.__token.getTag() in self.__firstEPrime:
			if self.__token.getTag() == ord('+'):
				self.__check(ord('+'))
				self.__T()
				self.__EPrime()
			elif self.__token.getTag() == ord('-'):
				self.__check(ord('-'))
				self.__T()
				self.__EPrime()
		else:
			pass

	def __TPrime(self):
		if self.__token.getTag() in self.__firstTPrime:
			if self.__token.getTag() == ord('*'):
				self.__check(ord('*'))
				self.__F()
				self.__TPrime()
			elif self.__token.getTag() == ord('/'):
				self.__check(ord('/'))
				self.__F()
				self.__TPrime()
		else:
			pass