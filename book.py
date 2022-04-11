class Book:
    def __init__(self,name = "new book",id = 101,author = "XYZ",year = 1990,status = 1):
        self.name = name
        self.id = id
        self.author = author
        self.year = year
        self.status = status
    def __str__(self):
        data = str(self.name) +","+ str(self.id)+ "," + str(self.author) + "," + str(self.year)+","+str(self.status)
        return data


if (__name__ == "__main__"):
    B1 = Book("James",102,"James",1992)
    print(B1)
