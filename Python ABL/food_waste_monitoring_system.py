
number_of_days = int(input("Enter number of days to monitor: "))

total_prepared = 0
total_served = 0
total_wasted = 0
valid_days = 0

if number_of_days <= 0:
    print("Invalid number of days.")

else:
    for i in range(number_of_days):
        print("\nDay", i + 1)

        food_prepared = float(
            input("Enter food prepared (kg): ")
        )

        food_served = float(
            input("Enter food served (kg): ")
        )

        food_wasted = float(
            input("Enter food wasted (kg): ")
        )

        if (food_prepared < 0 or
            food_served < 0 or
            food_wasted < 0):

            print("Invalid quantity. Values cannot be negative.")

        elif food_served + food_wasted > food_prepared:
            print("Invalid data. Served and wasted food cannot")
            print("exceed the quantity prepared.")

        else:
            remaining_food = (
                food_prepared - food_served - food_wasted
            )

            if food_prepared > 0:
                waste_percentage = (
                    food_wasted / food_prepared
                ) * 100
            else:
                waste_percentage = 0

            print("\n--- DAILY FOOD WASTE REPORT ---")
            print("Food prepared:", food_prepared, "kg")
            print("Food served:", food_served, "kg")
            print("Food wasted:", food_wasted, "kg")
            print("Remaining food:", remaining_food, "kg")
            print("Waste percentage:",
                  round(waste_percentage, 2), "%")

            if waste_percentage > 10:
                print("Waste status: High food waste")
            else:
                print("Waste status: Acceptable food waste")

            total_prepared = total_prepared + food_prepared
            total_served = total_served + food_served
            total_wasted = total_wasted + food_wasted
            valid_days = valid_days + 1

    print("\n--- OVERALL FOOD WASTE SUMMARY ---")
    print("Valid days recorded:", valid_days)
    print("Total food prepared:", total_prepared, "kg")
    print("Total food served:", total_served, "kg")
    print("Total food wasted:", total_wasted, "kg")

    if total_prepared > 0:
        overall_waste_percentage = (
            total_wasted / total_prepared
        ) * 100

        print("Overall waste percentage:",
              round(overall_waste_percentage, 2), "%")
    else:
        print("Overall waste percentage: 0.0%")

    print("Monitoring completed.")
