# Store registered students
students = []

# Function to register a student
def register_student(name, student_id, course):
    # Check for empty fields
    if not name.strip() or not student_id.strip() or not course.strip():
        print("Error: All fields are required.")
        return

    # Check for duplicate student IDs
    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists.")
            return

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
    if not students:
        print("No students registered.")
        return

    # Display all student records
    for student in students:
        print("Name:", student["name"])
        print("Student ID:", student["id"])
        print("Course:", student["course"])
        print("--------------------")


# Main program
def main():
    # Keep the menu running
    while True:
        print("\nSTUDENT REGISTRATION SYSTEM")
        print("1. Register Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            course = input("Enter course: ")

            register_student(name, student_id, course)

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()