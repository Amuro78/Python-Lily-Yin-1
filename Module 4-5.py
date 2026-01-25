#Module 4-5
username="python"
password = "rules"
rounds =0

user_name =input("Please enter your username:")
password =input("Please enter your password:")

while rounds<5:
 if  user_name!="python" and password!="rules":
    user_name=input("Please enter your username again:")
    password=input("Please enter your password again:")
    rounds = rounds + 1

 elif user_name=="python" and password!="rules":
    password=input("Please enter your password again:")
    rounds = rounds + 1

 elif user_name!="python" and password=="rules":
    user_name=input("Please enter your username again:")

 elif username=="python" and password=="rules":
     print("Welcome.")
     break

if rounds==5:
    print("Access denied.")




