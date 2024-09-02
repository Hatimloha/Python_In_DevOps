import sys

type == sys.args[1]

if type == "t2.micro":
  print("it will charge you 2 dollar a day")

elif type == "t2.medium":
  print("it will charge you 4 dollar a day")

elif type == "t2.large":
  print("it will charge you 10 dollar a day")

else: 
  print("No, we camt create it for you")
