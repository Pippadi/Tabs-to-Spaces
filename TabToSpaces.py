print("This program replaces tabs with a specified number of spaces in a specified file.")
pathToFile = input("Enter the path for the file: ")
indentSize = int(input("Enter the the number of spaces each indent should be: "))
saveCopy = input("Do you want to save the edited file to a copy? (Y/blank): ")

with open(pathToFile, "r") as file:
    text = file.read()
    file.close()

indent = ""
for i in range(0, indentSize):
    indent += " "

if saveCopy:
    extPoint = pathToFile.rfind(".")
    pathToFile = pathToFile[:extPoint] + "Copy" + pathToFile[extPoint:]

newText = text.replace("\t", indent)
if newText != text:
    with open(pathToFile, "w") as file:
        file.write(text.replace("\t", indent))
        file.close()
    print("\nChanges made.")
else:
    print("\nNo changes to be made. File left unchanged.")