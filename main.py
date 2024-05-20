def get_grade_point(grade):
    if 70 <= grade <= 100:
        return 5
    elif 60 <= grade <= 69:
        return 4
    elif 50 <= grade <= 59:
        return 3
    elif 45 <= grade <= 49:
        return 2
    elif 40 <= grade <= 44:
        return 1
    elif 0 <= grade <= 39:
        return 0
    else:
        raise ValueError("Grade must be between 0 and 100.")

def get_grades(subjects):
    grades = []
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter your grade for {subject}: "))
                grade_point = get_grade_point(grade)
                grades.append(grade_point)
                break
            except ValueError as e:
                print(e)
                print("Invalid input. Please enter a Value between 0 and 100.")
    return grades

def calculate_gpa(grades, units):
    total_points = sum(grade * credit for grade, credit in zip(grades, units))
    total_credits = sum(units)
    return total_points / total_credits

def main():
    subjects = ["MTH101", "RSU-GET103", "PHY101", "PHY107", "CHM101", "CHM107", "GST111", "GET101", "CPE111"]
    units = [2, 2, 1, 2, 2, 1, 2, 2, 2]  
    
    name = input("Enter your name: ")
    print(f"Welcome {name}!")
    
    while True:
        choice = input("Do you want to calculate GPA or CGPA? (Enter 'GPA' or 'CGPA'): ").strip().upper()
        
        if choice == 'GPA':
            print("Please enter your grades (Between 0 and 100) for the following subjects:")
            grades = get_grades(subjects)
            gpa = calculate_gpa(grades, units)
            print(f"Dear {name}, Your GPA is: {gpa:.2f} / 5")
            break
        
        elif choice == 'CGPA':
            print("Please enter your grades for the first semester (Between 0 and 100):")
            grades_sem1 = get_grades(subjects)
            print("Please enter your grades for the second semester (Between 0 and 100):")
            grades_sem2 = get_grades(subjects)
            
            gpa_sem1 = calculate_gpa(grades_sem1, units)
            gpa_sem2 = calculate_gpa(grades_sem2, units)
            
            cgpa = (gpa_sem1 + gpa_sem2) / 2
            print(f"Dear {name}, Your CGPA is: {cgpa:.2f} / 5")
            break
        
        else:
            print("Invalid choice. Please enter 'GPA' or 'CGPA'.")

if __name__ == "__main__":
    main()
