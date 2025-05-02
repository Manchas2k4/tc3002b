class SymbolTable:
    table = {}
    previous = None

    def __init__(self, env = None):
        self.previous = env
        self.table = {}

    def getPrevious(self):
        return self.previous
    
    def lookup(self, variable):
        if variable in self.table:
            # The variable is a local to this scope.
            return self.table[variable]
        elif self.previous != None:
            # The variable maybe is declared in an upper scope.
            return self.previous.lookup(variable)
        else: 
            return None
    
    def insert(self, variable):
        if not variable in self.table:
            # the variable has not been declared.
            self.table[variable] = (None, None)
            return True
        else:
            # the variable has already been declared.
            return False
        
    def set(self, variable, type = None, value = None):
        env = self
        found = False
        while env != None:
            if variable in env.table:
                found = True
                break
            env = env.previous
        
        if found:
            # the variable is declared.
            env.table[variable] = (type, value)
            return True
        else: 
            # the variable is not declared.
            return False
