
cabin_class=input("Place enter your class of a cruise ship (Lux,A,B,C):")


if cabin_class == "Lux":
   print(" You have upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print(" You have above the car deck, equipped with a window.")
elif cabin_class == "B":
    print(" You have windowless cabin above the car deck.")
elif cabin_class == "C":
    print(" You have windowless cabin below the car deck.")
else:
  print("Invalid cabin class")