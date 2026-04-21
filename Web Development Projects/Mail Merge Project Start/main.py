#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("./Input/Letters/starting_letter.txt", "r") as file:
    letters = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    new_names = []
    for line in names:
        new_names.append(line.replace("\n", ""))

for n in range(len(new_names)):
    with open(f"./Output/ReadyToSend/letter_for_{new_names[n]}.txt", "w") as file:
        new_letters = letters.replace("[name]", new_names[n])
        file.write(new_letters)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp