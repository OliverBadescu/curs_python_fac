from carte import Carte
from membru_biblioteca import MembruBiblioteca
from biblioteca import Biblioteca

biblioteca = Biblioteca("Biblioteca Centrala")

carte1 = Carte("Ion", "Liviu Rebreanu", "ISBN-001")
carte2 = Carte("Enigma Otiliei", "George Calinescu", "ISBN-002")
carte3 = Carte("Morometii", "Marin Preda", "ISBN-003")
carte4 = Carte("Ultima noapte de dragoste", "Camil Petrescu", "ISBN-004")
carte5 = Carte("Baltagul", "Mihail Sadoveanu", "ISBN-005")

for carte in [carte1, carte2, carte3, carte4, carte5]:
    biblioteca.adauga_carte(carte)

membru1 = MembruBiblioteca("Andrei")
membru2 = MembruBiblioteca("Maria")
membru3 = MembruBiblioteca("Ion")

biblioteca.listeaza_carti_disponibile()

print("\nsim imprumuturi")
membru1.imprumuta_carte(carte1)
membru2.imprumuta_carte(carte2)
membru2.imprumuta_carte(carte3)

print("\n carte ocupata ")
membru3.imprumuta_carte(carte1)

biblioteca.listeaza_carti_disponibile()

print("\n returnare carte ")
membru1.returneaza_carte(carte1)

print("\n  imprumut dupa returnare ")
membru3.imprumuta_carte(carte1)

biblioteca.listeaza_carti_disponibile()
