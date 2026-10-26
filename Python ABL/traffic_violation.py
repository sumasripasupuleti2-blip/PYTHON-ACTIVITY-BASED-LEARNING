number_of_violations = int(input("Enter number of traffic violations: "))

total_penalty = 0
valid_violations = 0
invalid_violations = 0

if number_of_violations < 0:
    print("Invalid number of violations.")

else:
    for i in range(number_of_violations):
        print("\nViolation", i + 1)

        print("1. Overspeeding")
        print("2. No helmet")
        print("3. No seat belt")
        print("4. Signal violation")

        choice = input("Enter violation type (1-4): ")

        penalty = 0
        violation_name = ""

        if choice == "1":
            violation_name = "Overspeeding"

            speed_limit = float(input("Enter speed limit (km/h): "))
            vehicle_speed = float(input("Enter vehicle speed (km/h): "))

            if speed_limit < 0 or vehicle_speed < 0:
                print("Invalid speed entered.")
                invalid_violations = invalid_violations + 1

            elif vehicle_speed <= speed_limit:
                penalty = 0
                valid_violations = valid_violations + 1

            else:
                excess_speed = vehicle_speed - speed_limit

                if excess_speed <= 10:
                    penalty = 500
                else:
                    penalty = 1000

                valid_violations = valid_violations + 1

        elif choice == "2":
            violation_name = "No helmet"
            penalty = 500
            valid_violations = valid_violations + 1

        elif choice == "3":
            violation_name = "No seat belt"
            penalty = 500
            valid_violations = valid_violations + 1

        elif choice == "4":
            violation_name = "Signal violation"
            penalty = 1000
            valid_violations = valid_violations + 1

        else:
            print("Invalid violation type.")
            invalid_violations = invalid_violations + 1

        if choice in ["1", "2", "3", "4"]:
            if not (choice == "1" and
                    (speed_limit < 0 or vehicle_speed < 0)):
                print("Violation:", violation_name)
                print("Penalty: Rs.", penalty)
                total_penalty = total_penalty + penalty

    print("\n--- TRAFFIC VIOLATION REPORT ---")
    print("Valid violations:", valid_violations)
    print("Invalid entries:", invalid_violations)
    print("Total penalty: Rs.", total_penalty)
    print("Report completed.")
