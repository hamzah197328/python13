file_name = input("Enter the file name: ")
file = open(file_name, "w")

notes = input("Enter your notes: ")
file.write(notes)
file.close()

'''file = open(file_name, "r")
for line in file:
    print(line.strip())
file.close()'''

with open(file_name, "r") as f:
    for line in f:
        print(line.strip())

with open(file_name, "r") as f:
    for line in f:
        words = line.split()
        print(len(words), 'words in line:', line.strip())