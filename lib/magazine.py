class Magazine:
    all_magazines = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) <= 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value
    
    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.magazine == self]
    
    def contributors(self):
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None
    
    @classmethod
    def top_publisher(cls):
        from article import Article
        if not Article.all_articles:
            return None
        
        magazine_counts = {}
        for article in Article.all_articles:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
        
        return max(magazine_counts, key=magazine_counts.get) if magazine_counts else None
