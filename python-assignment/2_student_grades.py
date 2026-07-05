students = {}

while True:
    print("\n1. Add new student")
    print("2. Update existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"Student '{name}' added with grade '{grade}'.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"Grade for '{name}' updated to '{grade}'.")
        else:
            print(f"Student '{name}' not found.")

    elif choice == "3":
        if students:
            print("\nStudent Grades:")
            for name, grade in students.items():
                print(f"  {name}: {grade}")
        else:
            print("No students found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
