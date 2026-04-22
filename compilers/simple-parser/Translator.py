from SymbolTable import *
from Type import *

class Node:
    def eval(self, env):
        pass

class Numeric(Node):
    def eval(self, env):
        pass

class Logic(Node):
    def eval(self, env):
        pass

class Void(Node):
    def eval(self, env):
        pass

# --- NUMERIC --- #
class Number(Numeric):
    def __init__(self, value):
        self.value = value
    
    def eval(self, env):
        return self.value

class Identifier(Numeric):
    def __init__(self, name, line):
        self.name = name
        self.line = line

    def eval(self, env):
        result = env.lookup(self.name)
        if result != None:
            (_, value) = result
            return value
        else: 
            text = "Line " + str(self.line) + " - " + self.name + " has not been declared"
            raise Exception(text)

class Minus(Numeric):
    def __init__(self, right):
        self.right = right

    def eval(self, env):
        return -1 * float(self.right.eval(env))

class Add(Numeric):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        left = float(self.left.eval(env))
        right = float(self.right.eval(env))
        return left + right
    
