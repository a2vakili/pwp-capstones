class User(object):
    def __init__(self, name, email):
        self.name  = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        

    def __repr__(self):
        string_object = "User: {}, email: {}, books read: {} ".format(self.name,self.email,self.books)
        return string_object

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            print("These two users are the same")

    def read_book(book,rating = None) :
         self.books[book] = rating

    def get_average_ratings(self):
        number_of_books = len(self.books)
        for book in self.books:
            rating_values = self.books[book]
        avg_rating = rating_values / number_of_books
        return avg_rating

class Book(object):
     def __init__(self,title,isbn):
         self.title = title
         self.isbn = isbn
         self.ratings = []
     
     def get_title(self):
         return self.title
     
     def get_isbn(self):
         return self.isbn 

     def set_isbn(self,new_isbn):
         self.isbn = new_isbn 
         print("The isbn number has been updated.")

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self,other_book):
        if self.title == other_book.title and self.isbn == other_book.get_isbn:
            print("These two books are the same")

    def get_average_rating(self):
        for book in self.books:
            rating_values += self.books[book]     
        return rating_values / len(self.books)

     def __hash__(self):
        return hash((self.title, self.isbn))


class Tomerator(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(title, isbn)
        book = Book(title,isbn)
        return book

    def create_novel(title,isbn,author)
        fiction = Fiction(title,isbn author)
        return fiction    

    def create_non_fiction(title,subject,level,isbn):
         non_fictiion = Non_Fiction(title,subject,level,isbn)
         return non_fictiion

    def add_book_to_user(book,email,rating = None):
        user = self.users[email]
        if user == NULL:
            print("No user with email: {}".format(email)) 
        else:
            read_book(book,rating)
            add_rating(book,rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(name,email, books = None):
        user = User(name,email)
        if books != None:
            for book in books:
                add_book_to_user(book,email)

    def print_catalog(self):
        for book in self.books:
            print(book)  

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        number_of_times_read = 0
        for book, value in self.books.items():
            if value > number_of_times_read:
                number_of_times_read = value
                updated_book = book
        return updated_book

    def highest_rated_book(self):
        highest_average_rating = 0
        for book,value in self.books.items():
            avg_rating = book.get_average_rating()
            if  avg_rating > highest_average_rating:
                highest_average_rating = avg_rating
        return highest_average_rating

    def most_positive_user(self):
        highest_average_rating = 0
        for user,value in self.users.items():
            avg_rating = user.get_average_rating()
            if  avg_rating > highest_average_rating:
                highest_average_rating = avg_rating
        return highest_average_rating


                

class Fiction(Book):
     def __init__(self,author):
         super(Fiction,self).__init__()
         self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}.".format(self.title,self.author)


class Non_Fiction(Book):
     def __init__(self,subject,level):
        super(Non_Fiction,self).__init__()
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self:
        return "{} a {} manuel on {}".format(self.title,self.level,self.subject)



