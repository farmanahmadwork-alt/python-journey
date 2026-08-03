books = []

def menu():
    print("=======Library management System=======")
    print("1.Add Book")
    print("2.Show Book")
    print("3 Search Book")
    print("4.Issue Book")
    print("5.Return Book")
    print("6 Delete Book")
    print("7.Exit")

def add_book():
       name = input("Enter book name:")
       author = input("enter author name:")

       book = {
              "name":name,
              "author":author,
              "status":"Available"
              }
       books.append(book)
       print("book add successfully")


def show_book():
       if len(books) == 0:
          print("no book available:")
       else:
          print("=======all book=========")


          for book in books :
              print(f"book name :{book['name']}")
              print(f"author    :{book['author']}")
              print(f"status    :{book['status']}")
              print("----------------------------")


def search_book():

    search = input("enter book name:")
    found  = False

    for book in books:

        if book["name"].lower() == search.lower():
           print("book found:")
           print(f"book name :{book['name']}")
           print(f"author    :{book['author']}")
           print(f"status    :{book['status']}")
           print("----------------------------")

           found = True
           break
    if found == False:
        print("book not found")

def issue_book():

    issue = input("Enter Book Name to Issue: ")

    found = False

    for book in books:

        if book["name"].lower() == issue.lower():

            found = True

            if book["status"] == "Available":

                book["status"] = "Issued"

                print("Book Issued Successfully")

            else:

                print("Book Already Issued")

            break

    if found == False:
        print("Book Not Found")


def return_book():
                         
    return_name = input("Enter Book Name to Return: ")

    found = False

    for book in books:

        if book["name"].lower() == return_name.lower():

            found = True

            if book["status"] == "Issued":

                book["status"] = "Available"

                print("Book Returned Successfully")

            else:

                print("Book is Already Available")


            break

    if found == False:

        print("Book Not Found")


def delete_book():

    delete_name = input("Enter Book Name to Delete: ")

    found = False

    for book in books:

        if book["name"].lower() == delete_name.lower():

            books.remove(book)

            print("Book Deleted Successfully")

            found = True
            break

    if found == False:

        print("Book Not Found")

     
      
while True:
    menu()

    choice = input("Enter Your Choice:")
    
    if choice=="1":
       print("Choice =", choice)

    if choice == "1":
        print("Inside Add Book")
        add_book()
    elif choice=="2":
        show_book()
    elif choice=="3":
        search_book()
    elif choice=="4":
        issue_book()
    elif choice=="5":
        return_book()
    elif choice == "6":
         delete_book()
    elif choice=="7":
           print("Thank For Use Library Management system")
           break
    else:
           print("Invalid Choice")