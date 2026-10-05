import random
number_to_guess = random.randint(1, 1000)
guess = -1
amount = int(0)
abandon = False
while guess != number_to_guess:
    instruction = input("Entrez un nombre entre 1 et 1000 : ")
    if not instruction.isnumeric():
        if instruction == 'q':
            abandon = True
            break
        else:
            print("Input is invalid")
            continue
    guess = int(instruction)
    if guess < number_to_guess :
        print("C'est plus grand.")
    elif guess > number_to_guess :
        print("C' est plus petit.")
    amount +=1
if abandon:
    print(f"Tu es nul. Le nombre était {number_to_guess}.")
else:
    print(f"Bien joué ! Vous avez trouvé le nombre en {amount} essais.")