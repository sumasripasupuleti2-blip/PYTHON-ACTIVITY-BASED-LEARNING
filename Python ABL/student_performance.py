
number_of_subjects = int(input("Enter number of subjects: "))

subject_names = []
exam1_marks = []
exam2_marks = []
exam3_marks = []

total_exam1 = 0
total_exam2 = 0
total_exam3 = 0

valid_input = True

if number_of_subjects <= 0:
    print("Invalid number of subjects.")

else:
    for i in range(number_of_subjects):
        print("\nSubject", i + 1)

        subject = input("Enter subject name: ")

        mark1 = float(input("Enter marks in Examination 1: "))
        mark2 = float(input("Enter marks in Examination 2: "))
        mark3 = float(input("Enter marks in Examination 3: "))

        if (mark1 < 0 or mark1 > 100 or
            mark2 < 0 or mark2 > 100 or
            mark3 < 0 or mark3 > 100):

            print("Invalid marks. Marks must be between 0 and 100.")
            valid_input = False
            break

        subject_names.append(subject)
        exam1_marks.append(mark1)
        exam2_marks.append(mark2)
        exam3_marks.append(mark3)

        total_exam1 = total_exam1 + mark1
        total_exam2 = total_exam2 + mark2
        total_exam3 = total_exam3 + mark3

    if valid_input:
        print("\n--- STUDENT PERFORMANCE REPORT ---")

        for i in range(number_of_subjects):
            average = (
                exam1_marks[i] +
                exam2_marks[i] +
                exam3_marks[i]
            ) / 3

            print("\nSubject:", subject_names[i])
            print("Examination 1:", exam1_marks[i])
            print("Examination 2:", exam2_marks[i])
            print("Examination 3:", exam3_marks[i])
            print("Average marks:", round(average, 2))

            if exam3_marks[i] > exam1_marks[i]:
                print("Performance trend: Improving")

            elif exam3_marks[i] < exam1_marks[i]:
                print("Performance trend: Declining")

            else:
                print("Performance trend: Unchanged")

            if (exam1_marks[i] < 40 and
                exam2_marks[i] < 40 and
                exam3_marks[i] < 40):

                print("Warning: Consistently weak subject.")

        print("\n--- OVERALL EXAMINATION AVERAGES ---")

        print("Examination 1 average:",
              round(total_exam1 / number_of_subjects, 2))

        print("Examination 2 average:",
              round(total_exam2 / number_of_subjects, 2))

        print("Examination 3 average:",
              round(total_exam3 / number_of_subjects, 2))

        print("\nPerformance analysis completed.")
