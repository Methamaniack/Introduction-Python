print("Saisissez un nombre (en secondes).")
sec1 = int(input())
heure = sec1 // 3600
minute = sec1 % 3600 // 60
sec2 = sec1 % 3600 % 60
print(str(sec1)+" secondes sont égale à " + str(heure)+" heures, "+str(minute)+" minutes et "+str(sec2)+" secondes.")