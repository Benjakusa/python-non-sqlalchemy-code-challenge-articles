class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  
    
    @property
    def name(self):
        return self._name