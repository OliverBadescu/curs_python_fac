class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if carte.este_imprumutata:
            print(f"Cartea '{carte.titlu}' este deja imprumutata!")
            return False
        carte.este_imprumutata = True
        self.carti_imprumutate.append(carte)
        print(f"{self.nume} a imprumutat '{carte.titlu}'")
        return True

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat '{carte.titlu}'")
            return True
        print(f"{self.nume} nu are cartea '{carte.titlu}'")
        return False

    def __str__(self):
        return f"Membru: {self.nume}, Carti imprumutate: {len(self.carti_imprumutate)}"
