Import datetime
# Dictionary to store books
library = {}
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author: ")

    library[book_id] = {
        "name": name,
        "author": author,
        "issued": False,
        "student": None,
        "issue_date": None,
        "duration": 0
    }
    print(" Book added successfully!\n")

def view_books():
    if not library:
        print(" No books available.\n")
        return

    for book_id, details in library.items():
        print(f"\nID: {book_id}")
        print(f"Name: {details['name']}")
        print(f"Author: {details['author']}")
        print(f"Issued: {details['issued']}")
        if details['issued']:
            print(f"Issued to: {details['student']}")
    print()

def issue_book():
    book_id = input("Enter Book ID to issue: ")

    if book_id in library and not library[book_id]['issued']:
        student = input("Enter Student Name: ")
        duration = int(input("Enter duration (in days): "))

        issue_date = datetime.date.today()

        library[book_id]['issued'] = True
        library[book_id]['student'] = student
        library[book_id]['issue_date'] = issue_date
        library[book_id]['duration'] = duration

        print(" Book issued successfully!\n")
    else:
        print(" Book not available or already issued.\n")


# Return Book
def return_book():
    book_id = input("Enter Book ID to return: ")

    if book_id in library and library[book_id]['issued']:
        return_date = datetime.date.today()
        issue_date = library[book_id]['issue_date']
        duration = library[book_id]['duration']

        days_used = (return_date - issue_date).days

        fine = calculate_fine(days_used, duration)

        print(f"\nDays used: {days_used}")
        print(f"Fine: ₹{fine}")

        # Reset book
        library[book_id]['issued'] = False
        library[book_id]['student'] = None
        library[book_id]['issue_date'] = None
        library[book_id]['duration'] = 0

        print(" Book returned successfully!\n")
    else:
        print("Invalid Book ID or not issued.\n")


# Fine Calculation (Progressive per week)
def calculate_fine(days_used, allowed_days):
    if days_used <= allowed_days:
        return 0

    extra_days = days_used - allowed_days
    weeks = extra_days // 7 + 1

    fine = 0
    rate = 10  

    for i in range(weeks):
        fine += rate
        rate += 5 

    return fine
def menu():
    while True:
        print("\nLibrary Management System ")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print(" Invalid choice, try again.\n")
menu()
