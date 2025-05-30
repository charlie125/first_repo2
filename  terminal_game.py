
import random

hp = 20
enemy_hp = 20

print("Attack = 1")
print("Block = 2")
print("Heal = 3")

while True:
    enemy_attack = random.randint(1, 5)
    hit = random.randint(1, 5)
    heal = random.randint(1, 5)
    action = input("Please enter your move:")

    if action == "1":
        hp -= enemy_attack
        print(f"Your remaining hp : {hp}")
        print("You are selecting [Attack]!")
        enemy_hp -= hit
        print(f"Your damage : {hit} points.")
        print(f"Enemy's remaining hp : {enemy_hp}")

    elif action == "2":
        print("You are selecting [Block]!")
        print("Sucessfully block!")

    elif action == "3":
        hp -= enemy_attack
        print(f"Your remaining hp : {hp}")
        print("You are selecting [Heal]!")
        print(f"Your heal : {heal} points.")
        hp += heal
        print(f"Your hp are being healed : {hp}")

    else:
        print("Invaild value!")

    if hp <= 0:
        print("Game Over!")
        break
    elif enemy_hp <= 0:
        print("You Win!")
        break
# 123
