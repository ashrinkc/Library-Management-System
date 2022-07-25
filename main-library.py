import datetime
import programs
import File

class library():
    #infinite loop
    while(True):
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("        Welcome to Otaku Library    ")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("====>Enter 1. To Display the books")
        print("====>Enter 2. To Borrow a book")
        print("====>Enter 3. To add a book")
        print("====>Enter 4. To return a book")
        print("====>Enter 5. To exit")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        try:
            a=int(input("Select a choice from 1 to 5: "))
            print("++++++++++++++++++++++++++++++++++++++++")
            if(a==1):
                with open("Books.txt","r") as f:
                    lines=f.read()
                    print(lines) #displaying the books from the text file
       
            elif(a==2):
                File.files()
                programs.borrowBook()
                
            elif(a==3):
                programs.addbook()
                
            elif(a==4):
                File.files()
                programs.returnBook()
                
            elif(a==5):
                print("Thank you for visiting Otaku Library")
                break
            
            else:
                print("Invalid!!!!.Please select any choice from 1 to 5")
                
        except ValueError:
            print("Wrong Input.")
