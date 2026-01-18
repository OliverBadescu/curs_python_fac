preturi = {"mere": 1.0, "banane": 0.5, "portocale": 0.8, "mango": 1.5}

stoc = {"mere": 10, "banane": 20, "portocale": 15, "mango": 5}

vanzari = [("mere", 4), ("banane", 6), ("portocale", 10), ("mango", 2)]

venit_total = 0
for produs, cantitate in vanzari:
    venit_total += preturi[produs] * cantitate
    stoc[produs] -= cantitate

de_realimentat = set()
for produs, cantitate in stoc.items():
    if cantitate < 5:
        de_realimentat.add(produs)

print(f"Venit total: {venit_total} RON")
print("Stocuri ramase:")
for produs, cantitate in stoc.items():
    print(f"  - {produs}: {cantitate}")
print("Produse ce necesita realimentare:")
for produs in de_realimentat:
    print(f"  - {produs}")
