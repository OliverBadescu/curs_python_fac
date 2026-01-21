class Biblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adaugata in biblioteca")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea '{carte.titlu}' a fost stearsa din biblioteca")
            return True
        print(f"Cartea '{carte.titlu}' nu exista in biblioteca")
        return False

    def listeaza_carti_disponibile(self):
        disponibile = [c for c in self.carti if not c.este_imprumutata]
        print(f"\nCarti disponibile in {self.nume}:")
        if disponibile:
            for carte in disponibile:
                print(f"  - {carte}")
        else:
            print("  Nicio carte disponibila")
        return disponibile
