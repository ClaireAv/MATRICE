name = "\nLaurie"
# name1 = name + 1
def user_generator():
    file = open("logins.db", "a") 
    file.write(name) 
    contenu = file.readlines("logins.db")
    # file.write(contenu) 
    if name in contenu:
        file.write("name")
    file.close()

user_generator()



