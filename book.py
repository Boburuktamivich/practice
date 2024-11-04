class Book:
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def checkout(self):
        if self.availability:
            self.availability = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.availability = True
        print(f"'{self.title}' has been returned and is now available.")

    def calculate_late_fees(self, day):
        f = 1.2 
        if day > 0:
            t = day * f
            print(f"Late fee for '{self.title}': ${t:.2f}")
            return t
        else:
            print(f"No late fee for '{self.title}'.")
            return 0

x = Book("Atomic Habits", "James Clear", "9876543210")
x.checkout()
x.return_book()
x.calculate_late_fees(5)