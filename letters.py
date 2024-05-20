def get_grades(subjects):
    grade_values = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0
    }
    
    grades = []
    for subject in subjects:
        while True:
            grade = input(f"Enter your grade for {subject} (A, B, C, D, E, F): ").strip().upper()
            if grade in grade_values:
                grades.append(grade_values[grade])
                break
            else:
                print("Invalid grade. Please enter a valid grade (A, B, C, D, E, F).")
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
            print("Please enter your grades for the following subjects:")
            grades = get_grades(subjects)
            gpa = calculate_gpa(grades, units)
            print(f"Dear {name}, Your GPA is: {gpa:.2f} / 5")
            break
        
        elif choice == 'CGPA':
            print("Please enter your grades for the first semester:")
            grades_sem1 = get_grades(subjects)
            print("Please enter your grades for the second semester:")
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
