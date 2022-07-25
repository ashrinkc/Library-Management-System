import datetime
import File #importing python file named File
# to borrow book
def borrowBook():

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    issue=False
    while(True):
        Name=input("Enter your name: ")
        if Name.isalpha(): #isalpha is a built-in-method that returns true if all characters in the string are alphabets(a-z)
            break
        print("please do not input digits")
                
    borrow="Issued-by-"+Name+".txt" #generating a text file
    with open(borrow,"w+") as f:
        f.write("------------------Otaku Library------------------  \n")
        f.write("Book Borrowed By: "+ Name+"\n")
        f.write("++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        f.write("Borrowed Date: " + current_date +"\n\n")
        f.write("-------------------------------------------------- \n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )

    while issue==False:
        print("Please select the book you want to borrow:")
        for i in range(len(File.bookname)):
            print("Enter", i, "to borrow book", File.bookname[i])
            print("---------------------------------------------------")
        
        try:   
            a=int(input())
            try:
                if(int(File.quantity[a])>0):
                    print("Book is available.You have borrowed this book!!!")
                    with open(borrow,"a") as f:
                        f.write("1. \t\t"+ File.bookname[a]+"\t\t  "+File.authorname[a]+"\n")
                        f.write("++++++++++++++++++++++++++++++++++++++++++++++++++ \n")

                    File.quantity[a]=int(File.quantity[a])-1 #decreasing the quantity by 1
                    with open("books.txt","w+") as f:
                        for i in range(6):
                            f.write(File.bookname[i]+","+File.authorname[i]+","+str(File.quantity[i])+","+"$"+File.cost[i]+"\n")

                    # to borrow more than one book
                    z=True
                    NUMBER=1
                    while z==True:
                        choice=str(input("You have borrowed a book would you like to borrow another one? Press y for yes and n for no."))
                        if(choice.upper()=="Y"): # if you want to borrow more books
                            NUMBER=NUMBER+1 # incresing value of NUMBER by 1 so we can increase the S.N according to the book borrowed
                            print("Please select the book you want to borrow:")
                            for i in range(len(File.bookname)):
                                print("Enter", i, "to borrow book", File.bookname[i])
                                print("---------------------------------------------------")
                            a=int(input())
                            if(int(File.quantity[a])>0):
                                print("Book is available.You have borrowed this book!!!")
                                with open(borrow,"a") as f:
                                    f.write(str(NUMBER) +". \t\t"+ File.bookname[a]+"\t\t  "+File.authorname[a]+"\n")
                                    f.write("++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
                                    

                                File.quantity[a]=int(File.quantity[a])-1 # decreasing quantity by 1
                                with open("books.txt","w+") as f:
                                    for i in range(6):
                                        f.write(File.bookname[i]+","+File.authorname[i]+","+str(File.quantity[i])+","+"$"+File.cost[i]+"\n")
                                        issue=False
                            else:
                                z=False
                                break
                        elif (choice.upper()=="N"): # if you dont want to borrow more books
                            print ("Thank you for borrowing books from Otaku Library. ")
                            print("")
                            z=False
                            issue=True
                        else:
                            print("Please select the given option")
                            
                else:
                    print("The selected book is currently not in the stock.Please borrow another book!!!")
                    return borrowBook()
                    issue=False
            except IndexError:
                print("No such book available!!!.Please choose again.")
        except ValueError:
            print("")
            print("Please choose as suggested.")

# to add books
def addbook():
        password = 2244
        a=int(input("enter the password:"))
        if(password==a):
            newbook = input("enter book name:")
            author = input("enter the author name:")
            quantity = int(input("enter the quantity:"))
            cost = int(input("enter the cost:"))             
            if newbook == "":
                return addbook()
            else:
                with open("Books.txt","a") as bl:
                    bl.writelines(newbook+","+author+","+str(quantity)+","+"$"+str(cost)) # adding book to the text file
                    print("The book has been added")
        else:
            print("You are not authorized")

# to return the borrowed book
def returnBook():
    name=input("Enter your name: ")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    a="Issued-by-"+name+".txt" # checking if the name is present in the database
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines] #strip removes $ from cost
        
        with open(a,"r") as f:
            d=f.read()
            print(d)
    except:
        print("No such borrower found!!!")
        returnBook()

    ret="Book-Return-by-"+name+".txt" #generating a text file 
    with open(ret,"w+")as f:
        f.write("---------------------Otaku Library------------------- \n")
        f.write("Book Returned By: "+ name+"\n")
        f.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        f.write("Return Date: " + current_date+"\n\n")
        f.write("----------------------------------------------------- \n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(6):
        if File.bookname[i] in d:
            with open(ret,"a") as f:
                f.write(str(i+1)+"\t\t"+File.bookname[i]+"\t\t$"+File.cost[i]+"\n")
                File.quantity[i]=int(File.quantity[i])+1
            total+=float(File.cost[i])
                
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Have you had this book for more than 10 days?")
    print("Press Y if Yes and N if No")
    info=input()
    if(info.upper()=="Y"):
        print("How many days has passed after the return date of the book has been expired?")
        day=int(input())
        fine=3*day
        with open(ret,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine # adding fine to total
        

    print("Total: "+ "$"+str(total))
    with open(ret,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
        
            
    with open("books.txt","w+") as f: #updating the text file
            for i in range(6):
                f.write(File.bookname[i]+","+File.authorname[i]+","+str(File.quantity[i])+","+"$"+File.cost[i]+"\n")





