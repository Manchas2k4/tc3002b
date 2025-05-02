from SymbolTable import *
from Type import *
import turtle

class Node:
	def eval(self, env, aTurtle):
		pass

class Numeric(Node):
	def eval(self, env, aTurtle):
		pass

class Logic(Node):
	def eval(self, env, aTurtle):
		pass

class Character(Node):
	def eval(self, env, aTurtle):
		pass

class Void(Node):
	def eval(self, env, aTurtle):
		pass

#--------------------------- Numeric Subclasses ---------------------------#
class Number(Numeric):
	def __init__(self, value):
		self.value = value

	def eval(self, env, aTurtle):
		return self.value

class Identifier(Numeric):
	def __init__(self, name, line):
		self.line = line
		self.name = name

	def eval(self, env, aTurtle):
		result = env.lookup(self.name)
		if result != None:
			(_, value) = result
			return value
		else:
			text = 'Line ' + self.line + " - " + self.name + " has not been declared"
			raise Exception(text)
	
class Minus(Numeric):
	def __init__(self, right):
		self.right = right

	def eval(self, env, aTurtle):
		return -1 * float(self._right.eval(env, aTurtle))
	
class Add(Numeric):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = float(self.left.eval(env, aTurtle))
		right = float(self.right.eval(env, aTurtle))
		return (left + right)

"""
Implement

class Subtrat(Numeric):

class Multiply(Numeric):
"""
		
class Divide(Numeric):
	def __init__(self, left, right, line):
		self.line = line
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = float(self.left.eval(env, aTurtle))
		right = float(self.right.eval(env, aTurtle))
		if right != 0:
			return (left / right)
		else:
			text = 'Line ' + self.line + " - division by zero"
			raise Exception(text)
		
class Module(Numeric):
	def __init__(self, left, right, line):
		self.line = line
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = float(self.left.eval(env, aTurtle))
		right = float(self.right.eval(env, aTurtle))
		if right != 0:
			return (left % right)
		else:
			text = 'Line ' + self.line + " - division by zero"
			raise Exception(text)
#--------------------------- Numeric Subclasses ---------------------------#

#--------------------------- Logic Subclasses ---------------------------#
class Boolean(Logic):
	def __init__(self, value):
		self.value = value

	def eval(self, env, aTurtle):
		return self.value
	
class Not(Logic):
	def __init__(self, right):
		self.right = right

	def eval(self, env, aTurtle):
		return not(bool(self.right.eval(env, aTurtle)))
	
class Lesser(Logic):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = float(self.left.eval(env, aTurtle))
		right = float(self.right.eval(env, aTurtle))
		return (left < right)
	
class LesserOrEqual(Logic):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = float(self.left.eval(env, aTurtle))
		right = float(self.right.eval(env, aTurtle))
		return (left <= right)
	
"""
Implement

class Greater(Logic):

class GreaterOrEqual(Logic):

class Equal(Logic):

class Different(Logic):
"""

class And(Logic):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = bool(self.left.eval(env, aTurtle))
		right = bool(self.right.eval(env, aTurtle))
		return (left and right)

class Or(Logic):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def eval(self, env, aTurtle):
		left = bool(self.left.eval(env, aTurtle))
		right = bool(self.right.eval(env, aTurtle))
		return (left or right)
#--------------------------- Logic Subclasses ---------------------------#

#-------------------------- Character Subclasses ---------------------------#
class String(Character):
	def __init__(self, value):
		self.value = value

	def eval(self, env, aTurtle):
		return self.value
	
class ElementList(Character):
	def __init__(self, element, elementList = None):
		self.element = element
		self.elementList = elementList

	def eval(self, env, aTurtle):
		result = ""

		if isinstance(self.element, String):
			result = self.element.eval(env, aTurtle)
		elif isinstance(self.element, Numeric):
			result = f'{self.element.eval(env, aTurtle):.2f}'
		else:
			result = str(self.element.eval(env, aTurtle))

		if self.elementList != None:
			result = result + " " + self.elementList.eval(env, aTurtle)
		return result
#-------------------------- Character Subclasses ---------------------------#

#---------------------------- Void Subclasses -----------------------------#
class If(Void):
	def __init__(self, condition, sequence):
		self.condition = condition
		self.sequence = sequence

	def eval(self, env, aTurtle):
		env = SymbolTable(env)
		if bool(self.condition.eval(env, aTurtle)):
			self.sequence.eval(env, aTurtle)
		env = env.getPrevious()

class IfElse(Void):
	def __init__(self, condition, ifSequence, elseSequence):
		self.condition = condition
		self.isSequence = ifSequence
		self.elseSequence = elseSequence

	def eval(self, env, aTurtle):
		env = SymbolTable(env)
		if bool(self.condition.eval(env, aTurtle)):
			self.isSequence.eval(env, aTurtle)
		else:
			self.elseSequence.eval(env, aTurtle)
		env = env.getPrevious()

class While(Void):
	def __init__(self, condition, sequence):
		self.condition = condition
		self.sequence = sequence

	def eval(self, env, aTurtle):
		while (bool(self.condition.eval(env, aTurtle))):
			env = SymbolTable(env)
			self.sequence.eval(env, aTurtle)
			env = env.getPrevious()
	
class Print(Void):
	def __init__(self, element, elementList = None):
		self.element = element
		self.elementList = elementList

	def eval(self, env, aTurtle):
		text = self.element.eval(env, aTurtle)
		if self.elementList != None:
			text = text + " " + self.elementList.eval(env, aTurtle)
		aTurtle.write(text)

class PenWidth(Void):
	def __init__(self, expression):
		self.expression = expression

	def eval(self, env, aTurtle):
		value = int(self.expression.eval(env, aTurtle))
		aTurtle.pensize(value)

class Color(Void):
	def __init__(self, redExpression, greenExpression, blueExpression, line):
		self.line = line
		self.redExpression = redExpression
		self.greenExpression = greenExpression
		self.blueExpression = blueExpression

	def eval(self, env, aTurtle):
		red = int(self.redExpression.eval(env, aTurtle))
		if red < 0 or red > 255:
			text = 'Line ' + self.line + "expected a positive number between 0..255 in the red value."
			raise Exception(text)
		green = int(self.greenExpression.eval(env, aTurtle))
		if green < 0 or green > 255:
			text = 'Line ' + self.line + "expected a positive number between 0..255 in the blue value."
			raise Exception(text)
		blue = int(self.blueExpression.eval(env, aTurtle))
		if blue < 0 or blue > 255:
			text = 'Line ' + self.line + "expected a positive number between 0..255 in the green value."
			raise Exception(text)
		aTurtle.pencolor(red, green, blue)

class PenDown(Void):
	def eval(self, env, aTurtle):
		aTurtle.pendown()

class PenUp(Void):
	def eval(self, env, aTurtle):
		aTurtle.penup()

"""
Implement

class Arc(Void):

class Circle(Void):

class Clear(Void):
"""

class SetXY(Void):
	def __init__(self, xExpression, yExpression):
		self.xExpression = xExpression
		self.yExpression = yExpression

	def eval(self, env, aTurtle):
		x = int(self.xExpression.eval(env, aTurtle))
		y = int(self.yExpression.eval(env, aTurtle))
		aTurtle.setposition(x, y)

class SetX(Void):
	def __init__(self, expression):
		self.expression = expression

	def eval(self, env, aTurtle):
		x = int(self.expression.eval(env, aTurtle))
		aTurtle.setx(x)

class SetY(Void):
	def __init__(self, expression):
		self.expression = expression

	def eval(self, env, aTurtle):
		y = int(self.expression.eval(env, aTurtle))
		aTurtle.sety(y)

"""
Implement

class Left(Void):

class Right(Void):

class Backward(Void):

class Forward(Void):

class Home(Void):
"""

class Assigment(Void):
	def __init__(self, id, expression, line):
		self.line = line
		self.id = id
		self.expression = expression

	def eval(self, env, aTurtle):
		value = self.expression.eval(env, aTurtle)

		type = None
		if isinstance(self.expression, Numeric): 
			type = Type.NUMBER
			value = float(value)
		else: 
			type = Type.BOOLEAN
			value = bool(value)

		if not(env.set(self.id, type, value)):
			text = 'Line ' + str(self.line) + " - " + self.id + " is not declared"
			raise Exception(text)
		
class IdDeclaration(Void):
	def __init__(self, id, line):
		self.line = line
		self.id = id

	def eval(self, env, aTurtle):
		if not env.insert(self.id):
			text = 'Line ' + self.line + " - redeclaration of " + str(self.id)
			raise Exception(text)

class idDeclarationList(Void):
	def __init__(self, idDeclaration, idDeclarationList = None):
		self.idDeclaration = idDeclaration
		self.idDeclarationList = idDeclarationList

	def eval(self, env, aTurtle):
		self.idDeclaration.eval(env, aTurtle)
		if self.idDeclarationList != None:
			self.idDeclarationList.eval(env, aTurtle)

class Declaration(Void):
	def __init__(self, idDeclaration, idDeclarationList = None):
		self.idDeclaration = idDeclaration
		self.idDeclarationList = idDeclarationList

	def eval(self, env, aTurtle):
		self.idDeclaration.eval(env, aTurtle)
		if self.idDeclarationList != None:
			self.idDeclarationList.eval(env, aTurtle)

class StatementSequence(Void):
	def __init__(self, statement, statementSequence = None):
		self.statement = statement
		self.statementSequence = statementSequence

	def eval(self, env, aTurtle):
		self.statement.eval(env, aTurtle)
		if self.statementSequence != None:
			self.statementSequence.eval(env, aTurtle)

class Program(Void):
	def __init__(self, statementSequence):
		self.statementSequence = statementSequence

	def eval(self, env, aTurtle):
		pass

	def eval(self):
		myEnv = SymbolTable()

		myScreen = turtle.getscreen()
		myTurtle = turtle.Turtle()  
		turtle.mode("logo")
		turtle.colormode(255)

		self.statementSequence.eval(myEnv, myTurtle)

		turtle.done()