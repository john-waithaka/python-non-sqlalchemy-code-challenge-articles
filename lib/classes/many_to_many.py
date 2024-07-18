# class Article:
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
        
# class Author:
#     def __init__(self, name):
#         self.name = name

#     def articles(self):
#         pass

#     def magazines(self):
#         pass

#     def add_article(self, magazine, title):
#         pass

#     def topic_areas(self):
#         pass

# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     def articles(self):
#         pass

#     def contributors(self):
#         pass

#     def article_titles(self):
#         pass

#     def contributing_authors(self):
#         pass


#CODE FROM GEMINI

# class Article:
#   def __init__(self, author, magazine, title):
#     # Validate title length (5 to 50 characters)
#     if not 5 <= len(title) <= 50:
#       raise ValueError("Article title must be between 5 and 50 characters")
#     # Ensure title is a string
#     if not isinstance(title, str):
#       raise TypeError("Article title must be a string")

#     self.author = author
#     self.magazine = magazine
#     self.title = title

#   def __repr__(self):
#     return f"Article(author={self.author.name}, magazine={self.magazine.name}, title={self.title})"


# class Author:
#   def __init__(self, name):
#     # Validate name length (must be longer than 0 characters)
#     if not len(name):
#       raise ValueError("Author name cannot be empty")
#     # Ensure name is a string
#     if not isinstance(name, str):
#       raise TypeError("Author name must be a string")

#     self.name = name
#     self._articles = []  # Private list to store references to articles

#   def articles(self):
#     return self._articles.copy()  # Return a copy of the internal list

#   def magazines(self):
#     # Use set comprehension to get unique magazines
#     return {article.magazine for article in self._articles}

#   def add_article(self, magazine, title):
#     new_article = Article(self, magazine, title)
#     self._articles.append(new_article)
#     # Add this article to the magazine's internal list as well (assuming magazine has a similar method)
#     magazine.add_article(new_article)
#     return new_article

#   def topic_areas(self):
#     if not self._articles:
#       return None  # Return None if author has no articles

#     # Use set comprehension to get unique categories from magazines
#     return {article.magazine.category for article in self._articles}


# class Magazine:
#   def __init__(self, name, category):
#     # Validate name length (2 to 16 characters)
#     if not 2 <= len(name) <= 16:
#       raise ValueError("Magazine name must be between 2 and 16 characters")
#     # Ensure name is a string
#     if not isinstance(name, str):
#       raise TypeError("Magazine name must be a string")
#     # Validate category length (must be longer than 0 characters)
#     if not len(category):
#       raise ValueError("Magazine category cannot be empty")
#     # Ensure category is a string
#     if not isinstance(category, str):
#       raise TypeError("Magazine category must be a string")

#     self.name = name
#     self.category = category
#     self._articles = []  # Private list to store references to articles

#   def articles(self):
#     return self._articles.copy()  # Return a copy of the internal list

#   def contributors(self):
#     # Use set comprehension to get unique authors
#     return {article.author for article in self._articles}

#   def add_article(self, article):
#     # Validate that the article belongs to this magazine
#     if article.magazine != self:
#       raise ValueError("Article does not belong to this magazine")
#     self._articles.append(article)
#     return article

#   def article_titles(self):
#     if not self._articles:
#       return None  # Return None if magazine has no articles

#     # Use list comprehension to get a list of titles
#     return [article.title for article in self._articles]

#   def contributing_authors(self):
#     # Filter authors who have written more than 2 articles for this magazine
#     authors_with_count = {author: 0 for author in self.contributors()}
#     for article in self._articles:
#       authors_with_count[article.author] += 1

#     contributing_authors = [author for author, count in authors_with_count.items() if count > 2]
#     return contributing_authors if contributing_authors else None



#CODE FROM CHAT - but fails some tests

#tests that are failing
"""
FAILED Article in many_to_many.py title is an immutable string - AttributeError: can't set attribute
FAILED Author in many_to_many.py author name is of type str and cannot change - AttributeError: can't set attribute
FAILED Magazine in many_to_many.py magazine name is of type str and can change - ValueError: Name must be a string.
FAILED Magazine in many_to_many.py magazine name is between 2 and 16 characters, inclusive - ValueError: Name must be between 2 and 16 characters.
FAILED Magazine in many_to_many.py magazine category is of type str and can change - ValueError: Category must be a string.
FAILED Magazine in many_to_many.py magazine category has length greater than 0 - ValueError: Category must be longer than 0 characters.
"""

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        self.__validate_title()
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    def __validate_title(self):
        if not isinstance(self._title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(self._title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

class Author:
    def __init__(self, name):
        self._name = name
        self.__validate_name()

    @property
    def name(self):
        return self._name

    def __validate_name(self):
        if not isinstance(self._name, str):
            raise ValueError("Name must be a string.")
        if len(self._name) == 0:
            raise ValueError("Name must be longer than 0 characters.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines())) or None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.__validate_name()
        self.__validate_category()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.__validate_name()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
        self.__validate_category()

    def __validate_name(self):
        if not isinstance(self._name, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(self._name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")

    def __validate_category(self):
        if not isinstance(self._category, str):
            raise ValueError("Category must be a string.")
        if len(self._category) == 0:
            raise ValueError("Category must be longer than 0 characters.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        return [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2] or None




#CODE FROM BLACKBOX BUT FAILS A FEW TESTS

"""
FAILED Article in many_to_many.py title is an immutable string - Exception: Title must be a string
FAILED Author in many_to_many.py author name is of type str and cannot change - AssertionError: assert 'ActuallyTopher' == 'Carry Bradshaw'
FAILED Magazine in many_to_many.py magazine name is of type str and can change - Exception: Name must be a string
FAILED Magazine in many_to_many.py magazine name is between 2 and 16 characters, inclusive - Exception: Name must be between 2 and 16 characters
FAILED Magazine in many_to_many.py magazine category is of type str and can change - Exception: Category must be a string
FAILED Magazine in many_to_many.py magazine category has length greater than 0 - Exception: Category must be longer than 0 characters
FAILED Magazine in many_to_many.py returns author list who have written more than 2 articles for the magazine - assert [] is None
"""

# class Article:
#     all = []

#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title
#         Article.all.append(self)

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#         if not isinstance(value, str):
#             raise Exception("Title must be a string")
#         if not 5 <= len(value) <= 50:
#             raise Exception("Title must be between 5 and 50 characters")
#         self._title = value

#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, value):
#         if not isinstance(value, Author):
#             raise Exception("Author must be an instance of Author")
#         self._author = value

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, value):
#         if not isinstance(value, Magazine):
#             raise Exception("Magazine must be an instance of Magazine")
#         self._magazine = value


# class Author:
#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise Exception("Name must be a string")
#         if len(value) <= 0:
#             raise Exception("Name must be longer than 0 characters")
#         self._name = value

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set([article.magazine for article in self.articles()]))

#     def add_article(self, magazine, title):
#         return Article(self, magazine, title)

#     def topic_areas(self):
#         if not self.articles():
#             return None
#         return list(set([article.magazine.category for article in self.articles()]))


# class Magazine:
#     def __init__(self, name, category):
#         self.name = name
#         self.category = category

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise Exception("Name must be a string")
#         if not 2 <= len(value) <= 16:
#             raise Exception("Name must be between 2 and 16 characters")
#         self._name = value

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, value):
#         if not isinstance(value, str):
#             raise Exception("Category must be a string")
#         if len(value) <= 0:
#             raise Exception("Category must be longer than 0 characters")
#         self._category = value

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set([article.author for article in self.articles()]))

#     def article_titles(self):
#         if not self.articles():
#             return None
#         return [article.title for article in self.articles()]

#     def contributing_authors(self):
#         if not self.articles():
#             return None
#         authors = [article.author for article in self.articles()]
#         return [author for author in set(authors) if authors.count(author) > 2]




#SECOND SOLUTION FROM BLACKBOX - 9 tests failing

"""
FAILED Article in many_to_many.py title is an immutable string - Exception: Title cannot be changed
FAILED Article in many_to_many.py author is of type Author and mutable - Exception: Author cannot be changed
FAILED Article in many_to_many.py magazine is of type Magazine and mutable - Exception: Magazine cannot be changed
FAILED Author in many_to_many.py author name is of type str and cannot change - Exception: Name cannot be changed
FAILED Magazine in many_to_many.py magazine name is of type str and can change - Exception: Name must be a string
FAILED Magazine in many_to_many.py magazine name is between 2 and 16 characters, inclusive - Exception: Name must be between 2 and 16 characters
FAILED Magazine in many_to_many.py magazine category is of type str and can change - Exception: Category must be a string
FAILED Magazine in many_to_many.py magazine category has length greater than 0 - Exception: Category must be longer than 0 characters
FAILED Magazine in many_to_many.py returns author list who have written more than 2 articles for the magazine - assert [] is None
"""

# class Article:
#     all = []

#     def __init__(self, author, magazine, title):
#         self._author = author
#         self._magazine = magazine
#         self._title = title
#         Article.all.append(self)

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#         raise Exception("Title cannot be changed")

#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, value):
#         raise Exception("Author cannot be changed")

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, value):
#         raise Exception("Magazine cannot be changed")


# class Author:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         raise Exception("Name cannot be changed")

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set([article.magazine for article in self.articles()]))

#     def add_article(self, magazine, title):
#         return Article(self, magazine, title)

#     def topic_areas(self):
#         if not self.articles():
#             return None
#         return list(set([article.magazine.category for article in self.articles()]))


# class Magazine:
#     def __init__(self, name, category):
#         self._name = name
#         self._category = category

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise Exception("Name must be a string")
#         if not 2 <= len(value) <= 16:
#             raise Exception("Name must be between 2 and 16 characters")
#         self._name = value

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, value):
#         if not isinstance(value, str):
#             raise Exception("Category must be a string")
#         if len(value) <= 0:
#             raise Exception("Category must be longer than 0 characters")
#         self._category = value

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set([article.author for article in self.articles()]))

#     def article_titles(self):
#         if not self.articles():
#             return None
#         return [article.title for article in self.articles()]

#     def contributing_authors(self):
#         if not self.articles():
#             return None
#         authors = [article.author for article in self.articles()]
#         return [author for author in set(authors) if authors.count(author) > 2]