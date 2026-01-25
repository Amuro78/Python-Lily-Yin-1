numbers= []
while True:
    input1 =input("Enter a number(enter space to stop): ")
    if input1 ==" ":
        break
    try:
       number = int(input1)
       numbers.append(number)
    except ValueError:
       print("Not valid number,end.")

if numbers:
    max_number=max(numbers)
    print("The maximum number is ",max_number)
else:
    print("Not valid number")

if numbers:
    min_number=min(numbers)
    print("The minimum number is ",min_number)
else:
    print("Not valid number")

