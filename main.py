placeholder="name"
with open("invited_names.txt") as name_file:
    names=name_file.readlines()

with open("example.txt",) as letter_file:
    letter_content=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        name_letter=letter_content.replace(placeholder,stripped_name)
        print(name_letter)
        with open(f"inviting_letter_for_{stripped_name}.txt","w") as invite:
            invite.write(name_letter)



