class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                book.display_info()


def main():
    library = Library()

    while True:
        print("\nLibrary Management System:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == '2':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            print("Exiting the Library Management System. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

