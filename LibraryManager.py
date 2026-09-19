class LibrarySystem:
    def __init__(self) -> None:
        self.books=[]
    def add_book(self,id,title,author):
        new_book=Book(id,title,author,"available")
        self.books.append(new_book)
    def borrow_book(self,book_name):
        for book in self.books:
            if book.name==book_name:
                book.status="borrowed"
        print(f"The book is {book_name} not available ")
        
        

    def return_book(self,book_name):
        for book in self.books:
            if book.title==book_name:
                book.status="available"

        print(f"The book is {book_name} available")
        
        
              
    def available_books(self):
        results=[b for b  in self.books if b.status=="available"]
        print("available books: ")
        for r in results:
            print(f"Book inforamtion: Title: {r.title} Author:{r.author}")
    def barrowed_books(self):
        results=[b for b in self.books if b.status=="barrowed"]
        print("The barrowed books:")
        for r in results:
            print(f"Book informations:  Title: {r.title} Author:{r.author} ")


    
    




class Book:
    def __init__(self,id,title,author,available) -> None:
        self.id=id
        self.title=title
        self.author=author
        self.status=available





def library_manager():
    print("Welcome to the library manager")
    