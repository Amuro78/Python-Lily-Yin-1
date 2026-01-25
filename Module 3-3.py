gender=input("Please enter your gender (female or male): ")
hemoglobin_value = int(input("Please enter your hemoglobin value (g/l): "))

if gender=="female":
 if hemoglobin_value<117:
    print("Your hemoglobin value is too low.")
 if 117<=hemoglobin_value<=155:
    print("Your hemoglobin value is normal.")
 if hemoglobin_value>155:
    print("Your hemoglobin value is too high.")

elif gender=="male":
 if hemoglobin_value<134:
    print("Your hemoglobin value is too low.")
 if 134<=hemoglobin_value<=167:
    print("Your hemoglobin value is normal.")
 if hemoglobin_value>167:
    print("Your hemoglobin value is too high.")
