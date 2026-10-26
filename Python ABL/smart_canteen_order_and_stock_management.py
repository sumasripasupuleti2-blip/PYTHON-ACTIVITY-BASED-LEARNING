
food_items = ["Sandwich", "Veg Burger", "Samosa", "Juice"]
prices = [50, 80, 20, 30]
stock = [10, 8, 20, 15]

total_bill = 0
successful_orders = 0
rejected_orders = 0

number_of_orders = int(input("Enter number of orders: "))

if number_of_orders < 0:
    print("Invalid number of orders.")

else:
    for i in range(number_of_orders):
        print("\n--- CANTEEN MENU ---")

        for j in range(len(food_items)):
            print(j + 1, ".", food_items[j],
                  "- Rs.", prices[j],
                  "- Stock:", stock[j])

        item_number = int(input("Enter menu number: "))
        quantity = int(input("Enter quantity: "))

        if item_number < 1 or item_number > len(food_items):
            print("Invalid menu selection.")
            rejected_orders = rejected_orders + 1

        elif quantity <= 0:
            print("Invalid quantity.")
            rejected_orders = rejected_orders + 1

        else:
            item_index = item_number - 1

            if quantity > stock[item_index]:
                print("Insufficient stock for",
                      food_items[item_index])
                print("Available stock:", stock[item_index])
                rejected_orders = rejected_orders + 1

            else:
                cost = prices[item_index] * quantity

                stock[item_index] = (
                    stock[item_index] - quantity
                )

                total_bill = total_bill + cost
                successful_orders = successful_orders + 1

                print("Order successful.")
                print("Item:", food_items[item_index])
                print("Quantity:", quantity)
                print("Order cost: Rs.", cost)
                print("Remaining stock:", stock[item_index])

    print("\n--- CANTEEN BILL SUMMARY ---")
    print("Successful orders:", successful_orders)
    print("Rejected orders:", rejected_orders)
    print("Total bill: Rs.", total_bill)

    print("\n--- UPDATED STOCK REPORT ---")

    for i in range(len(food_items)):
        print(food_items[i], ":", stock[i], "units remaining")

    print("\nOrder processing completed.")
