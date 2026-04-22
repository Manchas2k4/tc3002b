class SymbolTable:
    table = {}
    previous = None
    

    def __init__(self, env=None):
        self.previous = env
        self.table = {}

    def getPrevious(self):
        return self.previous
    
    def lookup(self, variable):
        if variable in self.table:
            return self.table[variable]
        elif self.previous != None:
            return self.previous.lookup(variable)
        else:
            return None
    
    def insert(self, variable):
        if not variable in self.table:
            self.table[variable] = (None, None)
            return True
        else:
            return False
        
    def set(self, variable, type = None, value = None):
        env = self
        found = False

        while env != None:
            if variable in env.table:
                found = True
                break
            env =env.previous
        
        if found:
            env.table[variable] = (type, value)
            return True
        else:
            return False