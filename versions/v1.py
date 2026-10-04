# Store registered students
students = []

# Function to register a student
def register_student(name, student_id, course):
    # Store student information
    student = {
        "name": name,
        "id": student_id,
        "course": course
    }

    # Add student to the list
    students.append(student)
    print("Student registered successfully!")


# Function to display students
def display_students():
    # Show all registered students
    for student in students:
        print("Name:", student["name"])
        print("Student ID:", student["id"])
        print("Course:", student["course"])
        print("--------------------")


# Main program
def main():
    # Display the menu
    while True:
        print("\nSTUDENT REGISTRATION SYSTEM")
        print("1. Register Student")
        print("2. View Students")
        print("3. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Get student information
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            course = input("Enter course: ")

            # Register the student
            register_student(name, student_id, course)

        elif choice == "2":
            # Display registered students
            display_students()

        elif choice == "3":
            # Exit the program
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


# Run the program
if __name__ == "__main__":
    main()