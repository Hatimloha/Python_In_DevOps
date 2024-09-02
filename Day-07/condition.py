import sys

type = sys.argv{1}

if type == "t2.micro":
  print("yes we can create it for you")
else:
  print("No, we can create it for you")


# Run File:
python3 condition.py t2.micro

# Output: yes we can create it for you

# Run File:
python3 condition.py t2.large

# Output: No, we can create it for you
