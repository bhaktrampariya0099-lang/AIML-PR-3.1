students = [
    {
        "Student ID": 101,
        "Name": "Priyanshu",
        "Age": 20,
        "Grade": "A",
        "Date of Birth": "2003-01-15",
        "Personal_Info": (101, "2003-01-15"),
        "Subjects": {"Math", "Science", "English"}
    },
    {
        "Student ID": 102,
        "Name": "Aryan",
        "Age": 22,
        "Grade": "B",
        "Date of Birth": "2001-05-20",
        "Personal_Info": (102, "2001-05-20"),
        "Subjects": {"Physics", "Chemistry", "Biology"}
    },
    {
        "Student ID": 103,
        "Name": "Meet",
        "Age": 18,
        "Grade": "B+",
        "Date of Birth": "2004-10-14",
        "Personal_Info": (103, "2004-10-14"),
        "Subjects": {"Math", "Science", "English"}
    },
    {
        "Student ID": 104,
        "Name": "Riya",
        "Age": 21,
        "Grade": "A",
        "Date of Birth": "2002-09-10",
        "Personal_Info": (104, "2002-09-10"),
        "Subjects": {"History", "Geography", "Political Science"}
    },
    {
        "Student ID": 105,
        "Name": "Ananya",
        "Age": 19,
        "Grade": "A-",
        "Date of Birth": "2004-03-05",
        "Personal_Info": (105, "2004-03-05"),
        "Subjects": {"Math", "Science", "English"}
    },
    {
        "Student ID": 106,
        "Name": "Kabir",
        "Age": 23,
        "Grade": "B+",
        "Date of Birth": "2000-07-25",
        "Personal_Info": (106, "2000-07-25"),
        "Subjects": {"Physics", "Chemistry", "Biology"}
    },
    {
        "Student ID": 107,
        "Name": "Ishita",
        "Age": 20,
        "Grade": "A",
        "Date of Birth": "2003-11-30",
        "Personal_Info": (107, "2003-11-30"),
        "Subjects": {"Math", "Science", "English"}
    },
    {
        "Student ID": 108,
        "Name": "Rohan",
        "Age": 22,
        "Grade": "B",
        "Date of Birth": "2001-04-18",
        "Personal_Info": (108, "2001-04-18"),
        "Subjects": {"History", "Geography", "Political Science"}
    },
    {
        "Student ID": 109,
        "Name": "Saanvi",
        "Age": 19,
        "Grade": "A-",
        "Date of Birth": "2004-02-12",
        "Personal_Info": (109, "2004-02-12"),
        "Subjects": {"Math", "Science", "English"}
    },
    {
        "Student ID": 110,
        "Name": "Vivaan",
        "Age": 21,
        "Grade": "B+",
        "Date of Birth": "2002-08-08",
        "Personal_Info": (110, "2002-08-08"),
        "Subjects": {"Physics", "Chemistry", "Biology"}
    }
]


student_data = {}

for student in students:
    student_id = str(student["Student ID"])
    student_data[student_id] = student


while True:

    print("===== STUDENT DATA ORGANIZER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        student_id = input("Enter Student ID: ")

        if student_id in student_data:

            student = student_data[student_id]

            print("----- STUDENT FOUND -----")
            print(f"Student ID: {student['Student ID']}")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            print(f"DOB: {student['Date of Birth']}")
            print(f"Subjects: {', '.join(sorted(student['Subjects']))}")

        else:

            print("Student not found!")
            print("Enter New Student Details")

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth: ")

            subjects = input("Enter Subjects (comma separated): ").split(",")

            personal_info = (int(student_id), dob)

            student = {
                "Student ID": int(student_id),
                "Name": name,
                "Age": age,
                "Grade": grade,
                "Date of Birth": dob,
                "Personal_Info": personal_info,
                "Subjects": {s.strip() for s in subjects}
            }

            students.append(student)
            student_data[student_id] = student

            print("Student Added Successfully!")



    elif choice == "2":

        print("----- ALL STUDENTS -----")

        for student in students:

            print("----------------------")
            print(f"Student ID: {student['Student ID']}")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Grade: {student['Grade']}")
            print(f"DOB: {student['Date of Birth']}")
            print(f"Subjects: {', '.join(sorted(student['Subjects']))}")


    elif choice == "3":

        student_id = input("Enter Student ID to Update: ")

        if student_id in student_data:

            student = student_data[student_id]

            student["Name"] = input("Enter New Name: ")
            student["Age"] = int(input("Enter New Age: "))
            student["Grade"] = input("Enter New Grade: ")
            student["Date of Birth"] = input("Enter New DOB: ")

            subjects = input("Enter New Subjects: ").split(",")

            student["Subjects"] = {s.strip() for s in subjects}
            student["Personal_Info"] = (
                int(student_id),
                student["Date of Birth"]
            )

            print("Student Updated Successfully!")

        else:
            print("Student Not Found!")



    elif choice == "4":

        student_id = input("Enter Student ID to Delete: ")

        if student_id in student_data:

            student = student_data[student_id]

            students.remove(student)
            del student_data[student_id]

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found!")


    elif choice == "5":

        all_subjects = set()

        for student in students:
            all_subjects.update(student["Subjects"])

        print("----- SUBJECTS OFFERED -----")

        for subject in sorted(all_subjects):
            print(subject)



    elif choice == "6":

        print("Thank You For Using Student Data Organizer!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
