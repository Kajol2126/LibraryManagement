from datetime import datetime, timedelta
from os import path
class BookMgmt:
    def AddBook(self,b1):
        fp = open("BookInfo.txt","a")
        fp.write(str(b1))
        fp.write("\n")
        fp.close()
    def ShowBook(self):
        try:
            fp1 = open("BookInfo.txt","r")
        except:
            print("Book is not available")
        else:
            data = fp1.read()
            print(data)
            fp1.close()
    
    def DeleteBook(self,id):
        emplist = []
        flag = False
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt","r") as fp:
                for line in fp:
                        data = line.split(",")
                        
                        if (data[0] == str(id)):
                            print("Record Found \n",line)
                            flag = True
                            break
                        else:    
                            emplist.append(line)
                
            if(flag == False):
                print("Record not found")
            else:
                with open("BookInfo.txt","w") as fp:
                    for emp in emplist:
                        fp.write(emp)
        else:
            print("Record not found")

    def SearchById(self,id):
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt","r") as fp2:
                flag = False
                for line in fp2:
                    data = line.split(",")
                    if (data[0] == str(id)):
                        print("Record Found","\n",line)
                        flag = True
                        break
            if(flag == False):
                print("Record not exist")

        else:
            print("Book not Found")
        
    def SearchByName(self,name):
            if(path.exists("BookInfo.txt")):
                with open("BookInfo.txt","r") as fp:
                    flag = False
                    for line in fp:
                        data = line.split(",")

                        if (name in line):
                            print("Record Found\n",line)
                            flag = True
                            break
                                                           
                    else:
                        print("Record Not Found")  
            else:
                print("Record Not Found")      
    def SearchByAuthor(self,author):
            if(path.exists("BookInfo.txt")):
                with open("BookInfo.txt","r") as fp:
                    flag = False
                    for line in fp:
                        if(author in line):
                            print("Record Found\n",line)
                            flag = True
                            break                               
                    else:
                        print("Record Not Found")  
            else:
                print("Record Not Found")
    def SearchByYear(self,year):
            if(path.exists("BookInfo.txt")):
                with open("BookInfo.txt","r") as fp:
                    flag = False
                    for line in fp:
                        data = line.split(",")
                        if(data[3] == str(year)):
                            print("Record Found\n",line)
                            flag = True
                            break                               
                    else:
                        print("Record Not Found")  
            else:
                print("Record Not Found")  
    def EditBook(self,id):
        Booklist = []
        flag = False
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt","r") as fp:
                
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record Found\n",line)
                        ans  = input("Do you want to edit book name y/n : ")
                        if(ans.lower() == "y"):
                            data[1] = input("Enter Book Name: ")
                        ans = input("Do you want to edit Author of Book y/n : ")
                        if(ans.lower() == "y"):
                            data[2] = input("Enter Author of Book: ")
                        ans = input("Do you want to edit Book year y/n: ")
                        if(ans.lower()=="y"):
                            data[3] = input("Enter Book year: ")
                        line = ",".join(data)
                        line+="\n"
                    else:
                        Booklist.append(line)
            if(flag == False):
                print("Record Not Found....")
            else:
                with open("BookInfo.txt","w") as fp:
                    for bk in Booklist:
                        fp.write(bk)
                        fp.write("\n")
                
    def IssueBook(self,id):
        BookList = []
        flag = False
        if(path.exists("BookInfo.txt")):
            with open("BookInfo.txt","r") as fp4:
                
                for line in fp4:
                    data = line.split(",")
                    if ((data[0]) == str(id)):
                        print("Book Found\n",line)
                        if((int(data[4])) == 1):
                            StudentName = input("Enter Student Name: ")
                            DateOfIssue = input("Enter Issue Date(yyyy/mm/dd): ")
                            print("Book Issued Successfully and Deadline of submission is 10 days")
                            Book =  str(id)+","+StudentName+","+str(DateOfIssue)
                            with open("IssueBook.txt","a") as fp4:
                                fp4.write(str(Book))
                                fp4.write("\n")
                            flag = True
                            data[4] = "0\n"

                        else:
                            print("Book is already issued by someone")
                
                    line = ",".join(data)            
                    BookList.append(line)
            if(flag == False):
                print("Book not Found")
            else:    
                with(open("BookInfo.txt","w")) as fp4:
                    for line in BookList:
                        fp4.write(line)
                        fp4.write("\n")
        else:
            print("Book not Found")

    def SubmitBook(self,id):
        Booklist = []
        flag = False
        if(path.exists("IssueBook.txt")):
            with open("IssueBook.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    if(data[0] == str(id)):
                        print("Record found")
                        DateOfIssue = data[2] 
                        DateOfIssue = DateOfIssue.split("/")
                        
                        DateOfSubmit = input("Enter Submit Date of Book(dd/mm/yyyy): ")
                        DateOfIssue = datetime(int(DateOfIssue[2]),int(DateOfIssue[1]),int(DateOfIssue[0]))
                        DateOfSubmit = DateOfSubmit.split("/")
                        DateOfSubmit = datetime(int(DateOfSubmit[2]),int(DateOfSubmit[1]),int(DateOfSubmit[0]))
                        Total_Days = (DateOfSubmit - DateOfIssue).days
                        flag = True
                        
                        if(Total_Days <= 10):
                            print("---Successfully Submitted---")
                        else:
                            print("You have to pay for late submission")
                            late_fee = (Total_Days - 10) * 20
                            print("Fine is",late_fee)
                        flag = True
                    else:
                        Booklist.append(data)
                
                if(flag):
                    with open("IssueBook.txt","w") as fp:
                        for line in Booklist:
                            line = ",".join(line)
                            fp.write(line)
                    Booklist = []
                    with open("BookInfo.txt","r") as fp:
                        for line in fp:
                            
                            if(str(id) in line):
                                line = line.split(",")
                                line[4] = "1"
                                line = ",".join(line)
                            Booklist.append(line)

                    with open("BookInfo.txt","w") as fp:
                        for line in Booklist:
                            fp.write(line)
        else:
            print("Record Not Found")           

                                
                                

                        


                        


                            
          
    