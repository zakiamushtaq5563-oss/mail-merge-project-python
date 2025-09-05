# #TODO: Create a letter using starting_letter.docx 
# file = open("./input/letters/starting_letter.docx", "r")
# letter_content = file.read()
# placeholder = file.readline()
# names_list = open("./input/names/invited_names.txt", "r")
# # names_list = names.readline()

# for name in names_list:
#     name = name.strip()
#     x = letter_content.replace("[name]", name)
#     letter = open(f"./output/readytosend/{name}"+"_letter.docx",mode="w")
#     letter.write(x)
    
    print("its okay no problem")
#     letter.close()

# file.close()
    


    
    



PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as file_names:
    names =file_names.readlines()
    print(names)

with open("./input/letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        letter = letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"./output/readytosend/letter_for_{striped_name}.docx", "w") as completed_letter:
            completed_letter.write(letter)
        