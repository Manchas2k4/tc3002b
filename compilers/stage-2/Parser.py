from Lexer import *
from Translator import *
from Type import *

class Parser:
	lexer = None
	token = None

	def __init__(self, filepath):
		self.lexer = Lexer(filepath)
		self.token = None

		self.firstPrimaryExpression = set((Tag.ID, Tag.NUMBER, Tag.TRUE, Tag.FALSE, ord('(')))

		self.firstUnaryExpression = self.firstPrimaryExpression.union( set((ord('-'), ord('!'))) )

		self.firstExtendedMultiplicativeExpression = set((ord('*'), ord('/'), Tag.MOD))

		self.firstMultiplicativeExpression = self.firstUnaryExpression

		self.firstExtendedAdditiveExpression = set((ord('+'), ord('-')))

		## ADD THE OTHER FIRST SETS WE WILL BE USING ##

	def error(self, extra = None):
		text = 'Line ' + str(self.lexer.line) + " - " 
		if extra == None:
			text = text + "."
		else:
			text = text + extra
		raise Exception(text)

	def check(self, tag):
		if self.token.tag == tag:
			self.token = self.lexer.scan()
		else:
			text = 'Line ' + str(self.lexer.line) + " - expected "
			if tag != Tag.ID:
				text = text + str(Token(tag)) + " before " + str(self.token) 
			else:
				text = text + "an identifier before " + str(self.token) 
			self.error(text)
	
	def analize(self):
		self.token = self.lexer.scan()
		return self.program()

	def primaryExpression(self):
		if self.token.tag in self.firstPrimaryExpression:
			if self.token.tag == Tag.ID:
				# semantic action #
				current = self.token
				# semantic action #

				self.check(Tag.ID)

				# semantic action #
				return Identifier(current.value, self.lexer.line)
				# semantic action #
			elif self.token.tag == Tag.NUMBER:
				# semantic action #
				current = self.token
				# semantic action #

				self.check(Tag.NUMBER)

				# semantic action #
				return Number(current.value)
				# semantic action #
			elif self.token.tag == Tag.TRUE:
				self.check(Tag.TRUE)

				# semantic action #
				return Boolean(True)
				# semantic action #
			elif self.token.tag == Tag.FALSE:
				self.check(Tag.FALSE)

				# semantic action #
				return Boolean(False)
				# semantic action #
			elif self.token.tag == ord('('):
				self.check(ord('('))

				# semantic action #
				node = self.expression()
				# semantic action #

				self.check(ord(')'))

				# semantic action #
				return node
				# semantic action #
		else:
			self.error("expected a primary expression before " + str(self.token))
		
	def unaryExpression(self):
		if self.token.tag in self.firstUnaryExpression:
			if self.token.tag == ord('-'):
				self.check(ord('-'))

				# semantic action #
				right = self.unaryExpression()
				return Minus(right)
				# semantic action #
			elif self.token.tag == ord('!'):
				self.check(ord('!'))

				# semantic action #
				right = self.unaryExpression()
				return Not(right)
				# semantic action #
			else:
				# semantic action #
				return self.primaryExpression()
				# semantic action #
		else: 
			self.error("expected an unary expression before " + str(self.token))
		
	def extendedMultiplicativeExpression(self, left):
		if self.token.tag in self.firstExtendedMultiplicativeExpression:
			if self.token.tag == ord('*'):
				self.check(ord('*'))
				
				# semantic action #
				right = self.unaryExpression()
				node = Multiply(left, right)
				return self.extendedMultiplicativeExpression(node)
				# semantic action #
			elif self.token.tag == ord('/'):
				self.check(ord('/'))

				# semantic action #
				right = self.unaryExpression()
				node = Divide(left, right, self.lexer.line)
				return self.extendedMultiplicativeExpression(node)
				# semantic action #
			elif self.token.tag == Tag.MOD:
				self.check(Tag.MOD)
				
				# semantic action #
				right = self.unaryExpression()
				node = Module(left, right, self.lexer.line)
				return self.extendedMultiplicativeExpression(node)
				# semantic action #
		else:
			return left

	def multiplicativeExpression(self):
		if self.token.tag in self.firstMultiplicativeExpression:
			# semantic action #
			left = self.unaryExpression()
			return self.extendedMultiplicativeExpression(left)
			# semantic action #
		else:
			self.error("expected an multiplicative expression before " + str(self.token))
	
	def extendedAdditiveExpression(self, left):
		if self.token.tag in self.firstExtendedAdditiveExpression:
			if self.token.tag == ord('+'):
				self.check(ord('+'))
				
				# semantic action #
				right = self.multiplicativeExpression()
				node = Add(left, right)
				return self.extendedAdditiveExpression(node)
				# semantic action #
			elif self.token.tag == ord('-'):
				self.check(ord('-'))
				
				# semantic action #
				right = self.multiplicativeExpression()
				node = Subtrat(left, right)
				return self.extendedAdditiveExpression(node)
				# semantic action #
		else:
			return left

	def additiveExpression(self):
		if self.token.tag in self.firstAdditiveExpression:
			# semantic action #
			left = self.multiplicativeExpression()
			return self.extendedAdditiveExpression(left)
			# semantic action #
		else:
			self.error("expected an additive expression before " + str(self.token))

	def extendedRelationalExpression(self, left):
		if self.token.tag in self.firstExtendedRelationExpresion:
			if self.token.tag == ord('<'):
				self.check(ord('<'))
				
				# semantic action #
				right = self.additiveExpression()
				node = Lesser(left, right)
				return self.extendedRelationalExpression(node)
				# semantic action #
			elif self.token.tag == Tag.LEQ:
				self.check(Tag.LEQ)
				
				# semantic action #
				right = self.additiveExpression()
				node = LesserOrEqual(left, right)
				return self.extendedRelationalExpression(node)
				# semantic action #
			elif self.token.tag == ord('>'):
				self.check(ord('>'))

				# semantic action #
				right = self.additiveExpression()
				node = Greater(left, right)
				return self.extendedRelationalExpression(node)
				# semantic action #
			elif self.token.tag == Tag.GEQ:
				self.check(Tag.GEQ)
				
				# semantic action #
				right = self.additiveExpression()
				node = GreaterOrEqual(left, right)
				return self.extendedRelationalExpression(node)
				# semantic action #
		else:
			return left

	def relationalExpression(self):
		if self.token.tag in self.firstRelationalExpression:
			# semantic action #
			left = self.additiveExpression()
			return self.extendedRelationalExpression(left)
			# semantic action #
		else:
			self.error("expected an relational expression before " + str(self.token))

	## ADD MISSING METHODS ##

	def program(self):
		if self.token.tag in self.firstProgram:
			sequence = self.statementSequence()
			if self.token.tag == Tag.EOF:
				return Program(sequence)
			else:
				print(str(self.token))
				self.error("ilegal start of a statement")
		else:
			self.error("expected a statement before " + str(self.token))