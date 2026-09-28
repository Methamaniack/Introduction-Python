age = int(input("Indique ton âge : "))
imax = str(input("Ton film est-il en IMAX ? (oui/non) ")
if imax == "oui" or imax == "Oui":
    tarifbase = 18.50
else:
    tarifbase = 14.10
special = str(input("As-tu droit à une réduction ? (oui/non) ")
if special == "oui" or special == "Oui":
    print(f"Ton billet coûte : {tarifbase/2}")
elif age < 18 or age > 64:
    print(f"Ton billet coûte : {tarifbase-4}")