print("Saisissez votre année de naissance.")
age = 2026-int(input())
print("Tu auras "+str(age)+" and à la fin de l'année.")
if 0 < age < 12 :
    print("Tu es un enfant.")
elif 11 < age < 18 :
    print("Tu es un adolescent.")
elif 17 < age < 120 :
    print("Tu es un adulte.")
else :
    print("Tu es très probablement mort.")