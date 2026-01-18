talent1=float(input("Please enter talents:"))
pound1=float(input("Please enter pound:"))
lot1=float(input("Please enter lot:"))

total_grams= lot1*13.3 + pound1*32*13.3 + talent1*20*32*13.3

kilograms= int(total_grams/1000)
grams= total_grams - (kilograms * 1000)
print(f"{kilograms} kilograms and {grams:.2f} grams.")
