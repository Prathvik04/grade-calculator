"""
Week 1 Miniproject: CLI Grade Calculator
------------------------------------------
Covers: functions, loops, and dictionaries.

Stores multiple students' grades in a dictionary like:
    {
        "Alice": [90, 85, 92],
        "Bob":   [70, 65, 80]
    }

Menu-driven CLI:
    1. Add a student
    2. Add a grade to a student
    3. View a student's report
    4. View report for all students
    5. Exit
"""

# ---------------------------------------------------------
# Data storage
# ---------------------------------------------------------
# One dictionary holds everything: student name -> list of grades
students = {}


# ---------------------------------------------------------
# Core functions
# ---------------------------------------------------------
def add_student(name):
    """Add a new student with an empty list of grades."""
    if name in students:
        print(f"'{name}' already exists.")
    else:
        students[name] = []
        print(f"Added student: {name}")


def add_grade(name, grade):
    """Append a grade (0-100) to an existing student."""
    if name not in students:
        print(f"'{name}' not found. Add them first.")
        return
    if not (0 <= grade <= 100):
        print("Grade must be between 0 and 100.")
        return
    students[name].append(grade)
    print(f"Added grade {grade} for {name}.")


def calculate_average(grades):
    """Return the average of a list of grades, or 0 if empty."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_letter_grade(average):
    """Convert a numeric average into a letter grade."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def print_student_report(name):
    """Print a single student's grades, average, and letter grade."""
    if name not in students:
        print(f"'{name}' not found.")
        return

    grades = students[name]
    average = calculate_average(grades)
    letter = get_letter_grade(average)

    print(f"\n--- Report for {name} ---")
    print(f"Grades:  {grades}")
    print(f"Average: {average:.2f}")
    print(f"Letter:  {letter}")


def print_all_reports():
    """Loop through every student and print their report."""
    if not students:
        print("No students yet.")
        return

    print("\n=== Class Report ===")
    for name in students:
        print_student_report(name)

    # Bonus: overall class average across all students' grades
    all_grades = []
    for grades in students.values():
        all_grades.extend(grades)
    if all_grades:
        class_avg = calculate_average(all_grades)
        print(f"\nOverall class average: {class_avg:.2f}")


# ---------------------------------------------------------
# CLI menu loop
# ---------------------------------------------------------
def print_menu():
    print("\n===== Grade Calculator =====")
    print("1. Add a student")
    print("2. Add a grade")
    print("3. View one student's report")
    print("4. View full class report")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ").strip()
            grade_input = input("Enter grade (0-100): ").strip()
            try:
                grade = float(grade_input)
                add_grade(name, grade)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            name = input("Enter student name: ").strip()
            print_student_report(name)

        elif choice == "4":
            print_all_reports()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1-5.")


if __name__ == "__main__":
    main()
