liste = [1, 2, 3, 4, 5]
index = False
new = False
while index != -1:
    index = input("Index : ")
    if not index.isnumeric():
        print("Veuillez saisir un chiffre.")
        continue
    else:
        index = int(index)
    if index == -1:
        break
    while not new.isnumeric():
        new = input("Nouvelle valeur : ")
        if not new.isnumeric():
            print("Veuillez saisir un chiffre.")
            continue
        
    