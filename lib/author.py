class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  
    
    @property
    def name(self):
        return self._name
     @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) <= 0:
            raise ValueError("Name must be longer than 0 characters")
        # If name already exists (hasattr check), don't allow change
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value