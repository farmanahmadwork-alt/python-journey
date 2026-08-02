students = []

def menu():

    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. Show Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")


    # Add Student

def add_student():
        
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        city = input("Enter Student City: ")
        marks = input("Enter Student Marks: ")

        student = {
            "name": name,
            "age": age,
            "city": city,
            "marks": marks
        }

        students.append(student)

        print("Student Added Successfully")


    # Show Student
def show_student():
        

        if len(students) == 0:
            print("No Student Found")

        else:
            print("\n===== All Students =====")

            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("City:", student["city"])
                print("Marks:", student["marks"])
                print("--------------------")


    # Search Student
def search_student():
        
        search_name = input("Enter Student Name to Search: ")

        found = False

        for student in students:

            if student["name"] == search_name:

                print("\n===== Student Found =====")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("City:", student["city"])
                print("Marks:", student["marks"])

                found = True
                break

        if found == False:
            print("Student Not Found")


    # Update Student
def update_student():
        
        update_name = input("Enter Student Name to Update: ")

        found = False

        for student in students:

            if student["name"] == update_name:

                print("Student Found! Enter New Details")

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["city"] = input("Enter New City: ")
                student["marks"] = input("Enter New Marks: ")

                print("Student Updated Successfully")

                found = True
                break


        if found == False:
            print("Student Not Found")


    # Delete Student
def delete_student():

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:

            if student["name"] == delete_name:

                students.remove(student)

                print("Student Deleted Successfully")

                found = True
                break


        if found == False:
            print("Student Not Found")


while True:
        menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank You For Using Student Management System")
            break

        else:
            print("Invalid Choice")

        