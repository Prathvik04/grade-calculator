# Week 1 Miniproject: CLI Grade Calculator

A simple command-line grade calculator built in Python. Covers core Week 1 fundamentals: functions, loops, and dictionaries.

## Features
- Add multiple students
- Add grades for each student
- View an individual student's report (grades, average, letter grade)
- View a full class report with an overall class average

## How to Run

\`\`\`bash
python grade_calculator.py
\`\`\`

## Menu Options

1. Add a student
2. Add a grade
3. View one student's report
4. View full class report
5. Exit

## Example Usage

\`\`\`
===== Grade Calculator =====
1. Add a student
2. Add a grade
3. View one student's report
4. View full class report
5. Exit
Choose an option (1-5): 1
Enter student name: Alice
Added student: Alice

Choose an option (1-5): 2
Enter student name: Alice
Enter grade (0-100): 90
Added grade 90.0 for Alice.

Choose an option (1-5): 3
Enter student name: Alice

--- Report for Alice ---
Grades:  [90.0]
Average: 90.00
Letter:  A
\`\`\`

## Grading Scale

| Average | Letter Grade |
|---------|--------------|
| 90–100  | A            |
| 80–89   | B            |
| 70–79   | C            |
| 60–69   | D            |
| Below 60 | F           |

## Concepts Used

- **Dictionaries** – storing student names mapped to lists of grades (`{"Alice": [90, 85, 92]}`)
- **Functions** – modular, single-purpose functions for each operation (add student, add grade, calculate average, etc.)
- **Loops** – a `while True` menu loop for the CLI, and `for` loops to iterate over students when generating reports

## Project Structure

\`\`\`
grade_calculator.py   # main script containing all logic
README.md             # this file
\`\`\`

## Author

Prathvik04
