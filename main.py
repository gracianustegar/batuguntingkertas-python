import random

pemain = input(
    "Tentukan pilihanmu!\n'g' untuk gunting, 'b' untuk batu, 'k' untuk kertas"
)

komputer = random.choice(['g', 'b', 'k'])

print("pilihan kamu: " + pemain)
print("pilihan komputer: " + komputer)
