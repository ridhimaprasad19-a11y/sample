Books=[]
issued_Books=[]
def add_Book():
    name=input("enter the book name:")
    Books.append(name)
    print(name,"is added successfully")

def show_books():
    if len(Books)==0:
        print('No Books available')
    else:
        print("Print available books")
        for b in Books:
            print(b)

def issue_Book():
    if len(Books)==0:
        print("no books available")
        return
    else:
        show_books()
        name=input("enter the book name you want")
        if name in Books:
           issued_Books.append(name)
           Books.remove(name)
           print(name,"is issued")
        else:
            print(name,"is not available")

def return_Book():
    name=input("enter the book you want to return")
    if name in issued_Books:
        issued_Books.remove(name)
        Books.append(name)
        print(name,"book returned")
    else:
        print(name,"book not issued")
def library():
    while True:
        print("Menu")
        print("1Add Book")
        print("2 Show Book")
        print("3 Issue Book")
        print("4 Return Book")
        print("5 Exit")
        Choice=int(input("Enter your Choice:"))
        if Choice==1:
            add_Book()
        elif Choice==2:
            show_books()
        elif Choice==3:
            issue_Book()
        elif Choice==4:
            return_Book()
        elif Choice==5:
            print("Thankyou!")
            break    
library()