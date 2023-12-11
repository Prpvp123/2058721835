class Reader:
    def __init__(self, full_name, ticket_number, faculty, birth_date, phone):
        self.full_name = full_name
        self.ticket_number = ticket_number
        self.faculty = faculty
        self.birth_date = birth_date
        self.phone = phone

    def takeBook(self, book_count):
        print(f"{self.full_name} взял {book_count} книги")

    def returnBook(self, book_count):
        print(f"{self.full_name} вернул {book_count} книги")


reader1 = Reader("Петров В. В.", "12345",
                 "Информатика", "01.01.1990",
                 "123-456-7890")
reader1.takeBook(3)
reader1.returnBook(2)
