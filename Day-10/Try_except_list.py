import os
folders = input("give the folder name with space").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Enter the valid input")
        break
    print("=== listing file as per the folder -" + folder)
    
    for file in files:
        print(file)
    
