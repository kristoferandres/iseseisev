# 03.03.2022
# iseseisev töö
# Kristofer Andres

#matemaatika harjutused
import random
loop = 0
oige = 0
while loop != 10:
    loop += 1
    earv = random.randint(0,10)
    tarv = random.randint(0,10)
    ovastus = earv * tarv
    print(f"{loop}. {earv} * {tarv} = ?")
    kvastus = int(input("? = "))
    if ovastus == kvastus:
        print("õige")
        print("")
        oige +=1
    else:
        print("väär")
        print("")
print(f"vastasid {oige}/10 õigesti")
