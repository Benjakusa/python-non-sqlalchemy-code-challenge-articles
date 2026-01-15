# lib/article.py

class Article:
    # Class variable to store all article instances
    all_articles = []
    
    def __init__(self, author, magazine, title):
        # Validate title first
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        
        # Store the title - we'll use a different private name to avoid issues
        self.__title = title  # Double underscore for name mangling
        
        # Initialize other attributes
        self._author = None
        self._magazine = None
        
        # Set author and magazine
        self.author = author
        self.magazine = magazine
        
        # Add to all articles
        Article.all_articles.append(self)
    
    @property
    def title(self):
        # Getter for title - returns the stored title
        return self.__title
    
    @title.setter 
    def title(self, value):
        # This setter will be called when someone tries article.title = value
        # We ignore any attempt to change the title
        # Don't raise an error, just don't do anything
        pass
    
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