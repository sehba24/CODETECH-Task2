def input_grades():
    grades = {}
    print("Enter grades for different subjects or assignments (enter 'done' to finish):")
    while True:
        subject = input("Enter subject/assignment: ")
        if subject.lower() == 'done':
            break
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade
    return grades

def calculate_average(grades):
    total = sum(grades.values())
    count = len(grades)
    average = total / count
    return average

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def main():
    grades = input_grades()
    if not grades:
        print("No grades entered.")
        return

    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    gpa = calculate_gpa(average)

    print("\nGrade Summary:")
    print(f"Subjects/Assignments and Grades: {grades}")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
