budget = float(input("Enter your shopping budget (Rs.): "))
number_of_products = int(input("Enter number of products: "))

names = []
prices = []
quantities = []
costs = []

total_cost = 0

if budget < 0 or number_of_products < 0:
    print("Invalid budget or number of products.")

else:
    for i in range(number_of_products):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        price = float(input("Enter price per unit (Rs.): "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity.")
            print("Please run the program again with valid values.")
            break

        product_cost = price * quantity

        names.append(name)
        prices.append(price)
        quantities.append(quantity)
        costs.append(product_cost)

        total_cost = total_cost + product_cost

    if len(names) == number_of_products:
        print("\n--- SHOPPING BILL ---")

        for i in range(number_of_products):
            print(names[i], "- Rs.", round(costs[i], 2))

        print("Total shopping cost: Rs.", round(total_cost, 2))
        print("Available budget: Rs.", round(budget, 2))

        if total_cost <= budget:
            print("Shopping is within budget.")
            print("Remaining budget: Rs.", round(budget - total_cost, 2))

        else:
            excess_amount = total_cost - budget

            print("Budget exceeded by: Rs.", round(excess_amount, 2))
            print("\n--- SUGGESTED SHOPPING PLAN ---")
            print("Products are considered in the order entered.")

            remaining_budget = budget
            revised_total = 0

            for i in range(number_of_products):
                affordable_quantity = int(remaining_budget // prices[i])

                if affordable_quantity > quantities[i]:
                    affordable_quantity = quantities[i]

                revised_cost = prices[i] * affordable_quantity

                print(names[i], "- Original quantity:", quantities[i])
                print("Suggested quantity:", affordable_quantity)
                print("Suggested cost: Rs.", round(revised_cost, 2))

                remaining_budget = remaining_budget - revised_cost
                revised_total = revised_total + revised_cost

            print("Revised shopping total: Rs.", round(revised_total, 2))
            print("Budget remaining: Rs.", round(remaining_budget, 2))
