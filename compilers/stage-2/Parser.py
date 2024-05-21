from Lexer import *

class Parser:
	__lex = None
	__token = None

	def __init__(self, filepath):
		self.__lex = Lexer(filepath)
		self.__token = None

		self.__firstPrimaryExpression = set((Tag.ID, Tag.NUMBER, Tag.TRUE, Tag.FALSE, ord('(')))

		self.__firstUnaryExpression = self.__firstPrimaryExpression.union( set((ord('-'), ord('!'))) )
		
		self.__firstExtendedMultiplicativeExpression = set((ord('*'), ord('/'), Tag.MOD))

		self.__firstMultiplicativeExpression = self.__firstUnaryExpression

		self.__firstExtendedAdditiveExpression = set((ord('+'), ord('-')))

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
				text = text + str(Token(tag)) + " before " + str(self.__token) 
			else:
				text = text + "an identifier before " + str(self.__token) 
			self.__error(text)
	
	def analize(self):
		self.__token = self.__lex.scan()
		self.__program()

	def __primaryExpression(self):
		if self.__token.getTag() in self.__firstPrimaryExpression:
			if self.__token.getTag() == Tag.ID:
				self.__check(Tag.ID)
			elif self.__token.getTag() == Tag.NUMBER:
				self.__check(Tag.NUMBER)
			elif self.__token.getTag() == Tag.TRUE:
				self.__check(Tag.TRUE)
			elif self.__token.getTag() == Tag.FALSE:
				self.__check(Tag.FALSE)
			elif self.__token.getTag() == ord('('):
				self.__check('(')
				self.__expression()
				self.__check(')')
		else:
			self.error("expected a primary expression before " + str(self.__token))
		
	def __unaryExpression(self):
		if self.__token.getTag() in self.__firstPrimaryExpression:
			if self.__token.getTag() == ord('-'):
				self.__check(ord('-'))
				self.__primaryExpression()
			elif self.__token.getTag() == ord('!'):
				self.__check(ord('!'))
				self.__primaryExpression()
			else:
				self.__primaryExpression()
		else: 
			self.error("expected an unary expression before " + str(self.__token))
		
	def __extendedMultiplicativeExpression(self):
		if self.__token.getTag() in self.__firstExtendedMultiplicativeExpression:
			if self.__token.getTag() == ord('*'):
				self.__check(ord('*'))
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
			elif self.__token.getTag() == ord('/'):
				self.__check(ord('/'))
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
			elif self.__token.getTag() == Tag.MOD:
				self.__check(Tag.MOD)
				self.__unaryExpression()
				self.__extendedMultiplicativeExpression()
		else:
			pass

	def __multiplicativeExpression(self):
		if self.__token.getTag() in self.__firstMultiplicativeExpression:
			self.__unaryExpression()
			self.__extendedMultiplicativeExpression()
		else:
			self.error("expected an multiplicative expression before " + str(self.__token))
	
	"""
	Implement
	def __extendedAdditiveExpression(self):
	
	def __additiveExpression(self):
	
	def __extendedRelationalExpression(self):
	
	def __relationalExpression(self):
	
	def __extendedEqualityExpression(self):
	
	def __equalityExpression(self):
	
	def __extendedConditionalTerm(self):
	
	def __conditionalTerm(self):
	
	def __extendedConditionalExpression(self):
	
	def __conditionalExpression(self):
	
	def __expression(self):
	"""
	
	def __ifElseStatement(self):
		if self.__token.getTag() == Tag.IFELSE:
			self.__check(Tag.IFELSE)
			self.__expression()
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
		else:
			self.error("expected an IFELSE expression before " + str(self.__token))

	def __ifStatement(self):
		if self.__token.getTag() == Tag.IF:
			self.__check(Tag.IF)
			self.__expression()
			self.__check(ord('['))
			self.__statementSequence()
			self.__check(ord(']'))
		else:
			self.error("expected an IF expression before " + str(self.__token))

	def __conditionalStatement(self):
		if self.__token.getTag() in self.__firstConditionalStatement:
			if self.__token.getTag() == Tag.IF:
				self.__ifStatement()
			elif self.__token.getTag() == Tag.IFELSE:
				self.__ifElseStatement()
		else:
			self.error("expected an conditional expression before " + str(self.__token))

	"""
	Implement
	def __repetitiveStatement(self):
	"""
		
	def __structuredStatement(self):
		if self.__token.getTag() in self.__firstStructuredStatement:
			if self.__token.getTag() in self.__firstConditionalStatement:
				self.__conditionalStatement()
			elif self.__token.getTag() == Tag.REPEAT:
				self.__repetitiveStatement()
		else:
			self.error("expected an structured expression before " + str(self.__token))

	def __element(self):
		if self.__token.getTag() in self.__firstElement:
			if self.__token.getTag() == Tag.STRING:
				self.__check(Tag.STRING)
			elif self.__token.getTag() in self.__firstExpression:
				self.__expression()
		else:
			self.error("expected an element expression before " + str(self.__token))
		
	def __elementList(self):
		if self.__token.getTag() == ord(','):
			self.__check(ord(','))
			self.__element()
			self.__elementList()
		else:
			pass
		
	def __textStatement(self):
		if self.__token.getTag() == Tag.PRINT:
			self.__check(Tag.PRINT)
			self.__check(ord('['))
			self.__element()
			self.__elementList()
			self.__check(ord(']'))
		else:
			self.error("expected a PRINT statement before " + str(self.__token))

	def __penWidthStatement(self):
		if self.__token.getTag() == Tag.PENWIDTH:
			self.__check(Tag.PENWIDTH)
			self.__expression()
		else:
			self.error("expected a PENWIDTH statement before " + str(self.__token))

	def __colorStatement(self):
		if self.__token.getTag() == Tag.COLOR:
			self.__check(Tag.COLOR)
			self.__expression()
			self.__check(ord(','))
			self.__expression()
			self.__check(ord(','))
			self.__expression()
		else:
			self.error("expected a COLOR statement before " + str(self.__token))
		
	def __penDownStatement(self):
		if self.__token.getTag() == Tag.PENDOWN:
			self.__check(Tag.PENDOWN)
		else:
			self.error("expected a PENDOWN statement before " + str(self.__token))
		
	def __penUpStatement(self):
		if self.__token.getTag() == Tag.PENUP:
			self.__check(Tag.PENUP)
		else:
			self.error("expected a PENUP statement before " + str(self.__token))
		
	def __arcStatement(self):
		if self.__token.getTag() == Tag.ARC:
			self.__check(Tag.ARC)
			self.__expression()
			self.__check(ord(','))
			self.__expression()
		else:
			self.error("expected a ARC statement before " + str(self.__token))
		
	def __circleStatement(self):
		if self.__token.getTag() == Tag.CIRCLE:
			self.__check(Tag.CIRCLE)
			self.__expression()
		else:
			self.error("expected a CIRCLE statement before " + str(self.__token))
		
	def __clearStatement(self):
		if self.__token.getTag() == Tag.CLEAR:
			self.__check(Tag.CLEAR)
		else:
			self.error("expected a CLEAR statement before " + str(self.__token))

	def __drawingStatement(self):
		if self.__token.getTag() in self.__firstDrawingStatement:
			if self.__token.getTag() == Tag.CLEAR:
				self.__clearStatement()
			elif self.__token.getTag() == Tag.CIRCLE:
				self.__circleStatement()
			elif self.__token.getTag() == Tag.ARC:
				self.__arcStatement()
			elif self.__token.getTag() == Tag.PENUP:
				self.__penUpStatement()
			elif self.__token.getTag() == Tag.PENDOWN:
				self.__penDownStatement()
			elif self.__token.getTag() == Tag.COLOR:
				self.__colorStatement()
			elif self.__token.getTag() == Tag.PENWIDTH:
				self.__penWidthStatement()
		else:
			self.error("expected a drawing statement before " + str(self.__token))
	
	"""
	Implement

	def __setXYStatement(self):
	
	def __setXStatement(self):
	
	def __setYStatement(self):
	
	def __leftStatement(self):
	
	def __rightStatement(self):
	
	def __backwardStatement(self):
	
	def __forwardStatement(self):
	
	def __movementStatement(self):
	"""

	def __assigmentStatement(self):
		if self.__token.getTag() == Tag.ID:
			self.__check(Tag.ID)
			self.__check(Tag.ASSIGN)
			self.__expression()
		else:
			self.error("expected an ASSIGMENT statement before " + str(self.__token))
		
	def __identifierList(self):
		if self.__token.getTag() == ord(','):
			self.__check(ord(','))
			self.__check(Tag.ID)
			self.__identifierList()
		else:
			pass

	def __declarationStatement(self):
		if self.__token.getTag() == Tag.VAR:
			self.__check(Tag.VAR)
			self.__check(Tag.ID)
			self.__identifierList()
		else:
			self.error("expected a DECLARATION statement before " + str(self.__token))
		
	def __simpleStatement(self):
		if self.__token.getTag() in self.__firstSimpleStatement:
			if self.__token.getTag() == Tag.VAR:
				self.__declarationStatement()
			elif self.__token.getTag() == Tag.ID:
				self.__assigmentStatement()
			elif self.__token.getTag() in self.__firstMovementStatement:
				self.__movementStatement()
			elif self.__token.getTag() in self.__firstDrawingStatement:
				self.__drawingStatement()
			elif self.__token.getTag() == Tag.PRINT:
				self.__textStatement()
		else:
			self.error("expected a simple statement statement before " + str(self.__token))
		
	def __statement(self):
		if self.__token.getTag() in self.__firstStatement:
			if self.__token.getTag() in self.__firstSimpleStatement:
				self.__simpleStatement()
			elif self.__token.getTag() in self.__firstStructuredStatement:
				self.__structuredStatement()
		else:
			self.error("expected a statement before " + str(self.__token))
		
	def __statementSequence(self):
		if self.__token.getTag() in self.__firstStatementSequence:
			self.__statement()
			self.__statementSequence()
		else:
			pass

	def __program(self):
		if self.__token.getTag() in self.__firstProgram:
			self.__statementSequence()
			if self.__token.getTag() != Tag.EOF:
				print(str(self.__token))
				self.error("ilegal start of a statement")
