class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        status = "imprumutata" if self.este_imprumutata else "disponibila"
        return f"'{self.titlu}' de {self.autor} (ISBN: {self.isbn}) - {status}"
