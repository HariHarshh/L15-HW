
user_input = int(input("Enter your age:"))
if age < 0 or age > 120:
         print("Error: Age must be between 0 and 120.")
else:  
     if age % 2 == 0:
          print("The age is Even.")
     else:
         print("The age is Odd.")