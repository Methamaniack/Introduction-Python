print("""Bienvenue dans ce programme pour calculer ta moyenne (sur 20).
Tape 'q' à tout moment pour quitter la boucle.""")
note = 0
allnotes = 0
amount = 0
while note != "q":
    note = input("Insère une note sur 20 : ")
    if note.isnumeric():
        note = float(note)
        if 0<=note<=20:
            allnotes += note
            amount += 1
        else:
            print("Résultat trop petit ou grand")
    elif note != "q":
        print("Valeur invalide")
        
print(f"Ta moyenne est de {allnotes/amount}.")
        
            
    