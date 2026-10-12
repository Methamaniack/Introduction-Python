password = input("Saisissez votre mot de passe : ")
password2 = False
while password != password2 : 
    password2 = input("Confirmez votre mot de passe : ")
    if password2 == password :
        break
    else :
        print("Ton mot de passe ne correspond pas. ")
print("Ton compte a été créé. ")