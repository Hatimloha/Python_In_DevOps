import os
folders = input("give the folder name with space").split()

for folder in folders:
    files = os.listdir(folder)
    print("=== listing file as per the folder -" + folder)
    
    for file in files:
        print(file)
    
