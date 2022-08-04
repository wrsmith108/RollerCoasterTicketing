print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height < 150:
  print("Sorry, you are not tall enough for this ride.")
else:
  print("Welcome! Please buy a ticket from the agent.")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please by $7")
  else:
    print("Please pay $12")