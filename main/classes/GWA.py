subjects = {}  # Dictionary to store subjects

def add_subject(name, grade, credit_unit):
    if name in subjects:
        print("Subject already exists. Please modify instead.")
    else:
        subjects[name] = {"grade": grade, "credit_unit": credit_unit}
        print("Subject added successfully!")

def modify_subject(name):
    if name in subjects:
        print("Current details - Grade:", subjects[name]['grade'], "Credit Unit:", subjects[name]['credit_unit'])
        grade = float(input("Enter new grade: "))
        credit_unit = int(input("Enter new credit unit: "))
        subjects[name]["grade"] = grade
        subjects[name]["credit_unit"] = credit_unit
        print("Subject updated successfully!")
    else:
        print("Subject not found.")

def delete_subject(name):
    if name in subjects:
        del subjects[name]
        print("Subject deleted successfully!")
    else:
        print("Subject not found.")

def display_subjects():
    if not subjects:
        print("No subjects to display.")
    else:
        print("-------------------------------------------------------")
        print("Subject        | Grade        | Credit Unit")
        print("-------------------------------------------------------")
        for name, details in subjects.items():
            print(name, "         |", details['grade'], "        |", details['credit_unit'])
        print("-------------------------------------------------------")

def calculate_gwa():
    if not subjects:
        print("No subjects available to calculate GWA.")
        return

    total_weighted = 0
    total_units = 0
    print("\nCalculating GWA...")
    print("-----------------------------------------------------------------------------------")
    print("Subject            |        Grade        |     Credit Unit    |    Weighted Grade")
    print("-----------------------------------------------------------------------------------")
    for name, details in subjects.items():
        weighted_grade = details['grade'] * details['credit_unit']
        total_weighted += weighted_grade
        total_units += details['credit_unit']
        print(name, "              |", details['grade'], "               |", details['credit_unit'], "                |", weighted_grade)
    print("------------------------------------------------------------------------------------")

    if total_units > 0:
        gwa = (total_weighted * 100) /  (total_units * 100)  # Simpler rounding mechanism
        print("Total Weighted Grades:", total_weighted)
        print("Total Credit Units:", total_units)
        print("Your GWA is:", gwa )  # Simulate rounding by dividing
    else:
        print("Total credit units cannot be zero.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Subject")
        print("2. Modify Subject")
        print("3. Delete Subject")
        print("4. Display Subjects")
        print("5. Calculate GWA")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            credit_unit = int(input("Enter credit unit: "))
            add_subject(name, grade, credit_unit)
        elif choice == "2":
            name = input("Enter subject name to modify: ")
            modify_subject(name)
        elif choice == "3":
            name = input("Enter subject name to delete: ")
            delete_subject(name)
        elif choice == "4":
            display_subjects()
        elif choice == "5":
            calculate_gwa()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()