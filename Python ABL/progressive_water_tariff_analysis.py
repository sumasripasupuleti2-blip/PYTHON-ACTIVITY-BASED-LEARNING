
water_consumption = float(
    input("Enter water consumption in kL: ")
)

slab1_charge = 0
slab2_charge = 0
slab3_charge = 0

if water_consumption < 0:
    print("Invalid water consumption.")
    print("Consumption cannot be negative.")

else:
    if water_consumption <= 10:
        slab1_charge = water_consumption * 5

    elif water_consumption <= 20:
        slab1_charge = 10 * 5
        slab2_charge = (water_consumption - 10) * 8

    else:
        slab1_charge = 10 * 5
        slab2_charge = 10 * 8
        slab3_charge = (water_consumption - 20) * 12

    total_bill = slab1_charge + slab2_charge + slab3_charge

    print("\n--- WATER BILL SUMMARY ---")
    print("Water consumption:", water_consumption, "kL")

    print("First 10 kL charge: Rs.",
          round(slab1_charge, 2))

    print("Next 10 kL charge: Rs.",
          round(slab2_charge, 2))

    print("Above 20 kL charge: Rs.",
          round(slab3_charge, 2))

    print("Total water bill: Rs.",
          round(total_bill, 2))
