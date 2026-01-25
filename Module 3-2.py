
cabin_class=input("Place enter your class of a cruise ship (Lux,A,B,C):")


if cabin_class == "Lux":
    print(" Lux: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print(" A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print(" B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print(" C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")