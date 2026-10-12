pin = False
tries = 0
while pin != int(7482) :
    pin = input("Saisissez votre PIN à 4 chiffres : ")
    if not pin.isnumeric():
        print("Ceci n'est pas un PIN valide, réessayez.")
        continue
    pin = int(pin)
    if pin != int(7482):
        if tries == 0 : 
            print("Incorrect ... 2 essais restants")
        else :
            print("Incorrect ... 1 essai restant")
    else :
        break
    if tries == 2 :
        break
    tries += 1
if pin == int(7482):
    print("Code PIN correct")
else:
    print("Trop d'essais, code PIN refusé")