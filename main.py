#Primeiros projeto em python.

import base
import random

Rock = base.pedra
Paper = base.papel
Scissors = base.tesoura

user_choice = int(input("Vamos brincar de Pedra, Papel e Tesoura? Escolha 1 para Pedra , 2 para Papel e 3 para Tesoura:"))
computer_choice = random.randint(1, 3)
print(f"Escolha do computador: {computer_choice}")
if computer_choice == 1 and user_choice < 3:
    print(f"Você venceu! {base.trofeu}")
elif user_choice == 2 and computer_choice == 3:
    print(f"O Computador venceu{base.trofeu}")
elif user_choice == 2 and computer_choice == 1:
    print(f"Você venceu! {base.trofeu}")
elif user_choice == 1 and computer_choice == 2:
    print(f"O Computador venceu{base.trofeu}")
elif computer_choice == 3 and user_choice == 1:
    print(f"Você venceu! {base.trofeu}")
elif  user_choice == 3 and computer_choice == 2:
    print(f"Você venceu! {base.trofeu}")
elif user_choice == computer_choice:
    print(f"Empate! {base.draw}")


