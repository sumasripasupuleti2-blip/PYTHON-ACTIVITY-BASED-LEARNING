
total_classes = int(input("Enter total number of classes conducted: "))
attended_classes = int(input("Enter number of classes attended: "))

required_percentage = 75

if total_classes <= 0:
    print("Invalid input. Total classes must be greater than zero.")

elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input. Check the number of classes attended.")

else:
    attendance_percentage = (attended_classes / total_classes) * 100

    print("\n--- ATTENDANCE REPORT ---")
    print("Total classes conducted:", total_classes)
    print("Classes attended:", attended_classes)
    print("Current attendance:", round(attendance_percentage, 2), "%")

    if attendance_percentage >= required_percentage:
        print("Attendance requirement satisfied.")
        print("Additional classes required: 0")

    else:
        future_classes = 0
        future_total = total_classes
        future_attended = attended_classes

        while (future_attended / future_total) * 100 < required_percentage:
            future_classes = future_classes + 1
            future_total = future_total + 1
            future_attended = future_attended + 1

        print("Attendance requirement not yet satisfied.")
        print("Minimum consecutive classes to attend:", future_classes)

        final_percentage = (future_attended / future_total) * 100
        print("Attendance after attending these classes:",
              round(final_percentage, 2), "%")
