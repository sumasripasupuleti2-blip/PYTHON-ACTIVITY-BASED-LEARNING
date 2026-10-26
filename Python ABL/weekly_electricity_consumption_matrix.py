
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

daily_consumption = []
weekly_total = 0
valid_input = True

threshold = 10

print("--- WEEKLY ELECTRICITY CONSUMPTION ---")

for i in range(7):
    reading = float(
        input("Enter electricity consumption for " +
              days[i] + " (kWh): ")
    )

    if reading < 0:
        print("Invalid reading. Consumption cannot be negative.")
        valid_input = False
        break

    daily_consumption.append(reading)
    weekly_total = weekly_total + reading

if valid_input:
    average_consumption = weekly_total / 7

    highest_consumption = daily_consumption[0]
    highest_day = days[0]

    for i in range(7):
        if daily_consumption[i] > highest_consumption:
            highest_consumption = daily_consumption[i]
            highest_day = days[i]

    print("\n--- DAILY CONSUMPTION REPORT ---")

    for i in range(7):
        print(days[i], ":", daily_consumption[i], "kWh")

        if daily_consumption[i] > threshold:
            print("  Status: High consumption")
        else:
            print("  Status: Normal consumption")

    print("\n--- WEEKLY SUMMARY ---")
    print("Total weekly consumption:",
          round(weekly_total, 2), "kWh")

    print("Average daily consumption:",
          round(average_consumption, 2), "kWh")

    print("Highest consumption:",
          highest_consumption, "kWh")

    print("Day with highest consumption:", highest_day)

    high_days = 0

    for i in range(7):
        if daily_consumption[i] > threshold:
            high_days = high_days + 1

    print("Number of high-consumption days:", high_days)
    print("Weekly analysis completed.")
