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






#CODE 1 - but fails some tests



#tests that are failing
"""
FAILED Article in many_to_many.py title is an immutable string - AttributeError: can't set attribute
FAILED Author in many_to_many.py author name is of type str and cannot change - AttributeError: can't set attribute
FAILED Magazine in many_to_many.py magazine name is of type str and can change - ValueError: Name must be a string.
FAILED Magazine in many_to_many.py magazine name is between 2 and 16 characters, inclusive - ValueError: Name must be between 2 and 16 characters.
FAILED Magazine in many_to_many.py magazine category is of type str and can change - ValueError: Category must be a string.
FAILED Magazine in many_to_many.py magazine category has length greater than 0 - ValueError: Category must be longer than 0 characters.
"""

# class Article:
#     all = []

#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self._title = title
#         self.__validate_title()
#         Article.all.append(self)

#     @property
#     def title(self):
#         return self._title

#     def __validate_title(self):
#         if not isinstance(self._title, str):
#             raise ValueError("Title must be a string.")
#         if not (5 <= len(self._title) <= 50):
#             raise ValueError("Title must be between 5 and 50 characters.")

# class Author:
#     def __init__(self, name):
#         self._name = name
#         self.__validate_name()

#     @property
#     def name(self):
#         return self._name

#     def __validate_name(self):
#         if not isinstance(self._name, str):
#             raise ValueError("Name must be a string.")
#         if len(self._name) == 0:
#             raise ValueError("Name must be longer than 0 characters.")

#     def articles(self):
#         return [article for article in Article.all if article.author == self]

#     def magazines(self):
#         return list(set(article.magazine for article in self.articles()))

#     def add_article(self, magazine, title):
#         return Article(self, magazine, title)

#     def topic_areas(self):
#         return list(set(magazine.category for magazine in self.magazines())) or None

# class Magazine:
#     def __init__(self, name, category):
#         self._name = name
#         self._category = category
#         self.__validate_name()
#         self.__validate_category()

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value
#         self.__validate_name()

#     @property
#     def category(self):
#         return self._category

#     @category.setter
#     def category(self, value):
#         self._category = value
#         self.__validate_category()

#     def __validate_name(self):
#         if not isinstance(self._name, str):
#             raise ValueError("Name must be a string.")
#         if not (2 <= len(self._name) <= 16):
#             raise ValueError("Name must be between 2 and 16 characters.")

#     def __validate_category(self):
#         if not isinstance(self._category, str):
#             raise ValueError("Category must be a string.")
#         if len(self._category) == 0:
#             raise ValueError("Category must be longer than 0 characters.")

#     def articles(self):
#         return [article for article in Article.all if article.magazine == self]

#     def contributors(self):
#         return list(set(article.author for article in self.articles()))

#     def article_titles(self):
#         return [article.title for article in self.articles()] or None

#     def contributing_authors(self):
#         return [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2] or None




#CODE 2 BUT FAILS A FEW TESTS

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







"""Final code """


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")
            
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Author must be an instance of Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be an instance of Magazine")
    #pass.

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        #pass.


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")   

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        if (list_of_authors):
            return list_of_authors
        else:
            return None
        #pass.