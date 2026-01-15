class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

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
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class")
        self._magazine = value


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({mag.category for mag in self.magazines()})


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")

        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

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
        if not Article.all:
            return None
        magazine_counts = {}
        for article in Article.all:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
        return max(magazine_counts, key=magazine_counts.get) if magazine_counts else None
