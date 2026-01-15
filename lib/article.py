class Article:
    all_articles = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from author import Author
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        from magazine import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class")
        self._magazine = value
