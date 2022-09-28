pes: float; jarda: float; mil: float; pol: float

pes = float(input("Coloque sua media em PES: "))

jarda = pes / 3
pol = pes * 12
mil = jarda / 760

print(f"Sua medida em JARDA: {round(jarda,2)}")
print(f"Sua medida em POLEGADAS: {round(pol,2)}")
print(f"Sua medida em MILHAS: {round(mil,2)}")
