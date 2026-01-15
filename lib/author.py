class Author:
    all_authors = []
    
    def __init__(self, name):
        # Initialize author with name
        self._name = name
        # Add author to list of all authors
        Author.all_authors.append(self)
    
    @property
    def name(self):
        # Getter for name property
        return self._name
    
    @name.setter
    def name(self, value):
        # Name cannot be changed after instantiation
        # hasattr checks if attribute exists (was set in __init__)
        if hasattr(self, '_name'):
          return
        # Validate name type and length
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) <= 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value
    
    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.author == self]
    
    def magazines(self):
        magazine_list = [article.magazine for article in self.articles()]
        # Remove duplicates using set and return as list
        return list(set(magazine_list))
    
    def add_article(self, magazine, title):
        # Create new article linking this author to magazine
        from article import Article
        return Article(self, magazine, title)
    
    def topic_areas(self):
        # Return unique list of magazine categories author has written for
        if not self.articles():
            return None
        categories = [magazine.category for magazine in self.magazines()]
        return list(set(categories))