from book import Book
from bookMgmt import BookMgmt
def AdminMenuMgmt():
    bookMgmt = BookMgmt()
    ch = 0

    while(ch != 10):
        print('''
        1. Add Book
        2. View Book 
        3. Delete Book
        4. Search Book by Name
        5. Search Book by Author Name
        6. Search Book by Year
        7. Search Book by ID
        8. Edit Book
        ''')
        try:
            ch = int(input("Enter Your Choice: "))
        except:
            print("Please enter numeric value")
        else:
            if(ch == 1):
                id = int(input("Enter Book ID: "))
                name = input("Enter Book Name: ")
                author = input("Enter Book's Author Name: ")
                year = int(input("Enter Year of the Book: "))
                book = Book(id,name,author,year)
                bookMgmt.AddBook(book)
            elif(ch == 2):
                bookMgmt.ShowBook()
            elif(ch == 3):
                id = int(input("Enter Id to delete: "))
                bookMgmt.DeleteBook(id)
            elif(ch == 4):
                name = input("Enter Name: ")
                bookMgmt.SearchByName(name)
            elif(ch == 5):
                author = input("Enter Author of the book: ")
                bookMgmt.SearchByAuthor(author)
            elif(ch == 6):
                year = int(input("Enter Year of the Book You Want: "))
                bookMgmt.SearchByYear(year)
            elif(ch == 7):
                id = int(input("Enter Id: "))
                bookMgmt.SearchById(id)
            elif(ch == 8):
                id = int(input("Enter book id to edit: "))
                bookMgmt.EditBook(id)
            




if (__name__ == "__main__"):
    AdminMenuMgmt()