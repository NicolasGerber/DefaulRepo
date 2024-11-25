with open("../EstudosCtoPY/Input/names.txt", mode='r') as names:
    all_names = [name.strip() for name in names.readlines()]

with open("../EstudosCtoPY/Input/Letters/starting_letter.txt", mode='r') as letter:
    content = letter.read()
    for name in all_names:
       new_letter =  content.replace("[name]", name)
       with open(f"../EstudosCtoPY/Output/ReadyToSend/Letter_for_{name}.docx", mode="w") as complete_letter:
           complete_letter.write(new_letter)






