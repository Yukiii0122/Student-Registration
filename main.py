# Store registered students in a list
students = []

# Function to register a new student
def register_student(name, student_id, course):

    # Check if any required field is empty
    if not name.strip() or not student_id.strip() or not course.strip():
        print("Error: All fields are required.")
        return

    # Check if the student ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists.")
            return

    # Store the student's information in a dictionary
    student = {
        "name": name,
        "id": student_id,
        "course": course
    }

    # Add the student to the list
    students.append(student)
    print("Student registered successfully!")


# Function to display all registered students
def display_students():

    # Check if there are no registered students
    if not students:
        print("No students registered.")
        return

    # Display the information of each student
    for student in students:
        print("Name:", student["name"])
        print("Student ID:", student["id"])
        print("Course:", student["course"])
        print("--------------------")


# Main function to control the program
def main():

    
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

if __name__ == "__main__":
    main()
