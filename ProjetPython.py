class Library:
    # Méthode d'initialisation de la classe Library
    def __init__(self, name, employees=None, books=None):
        # On définit le nom de la bibliothèque
        self.name = name
        # Si aucun employé n'a été spécifié, on initialise une liste vide d'employés
        if employees is None:
            self.employees = []
        # Sinon, on utilise la liste d'employés donnée
        else:
            self.employees = employees
        # Si aucun livre n'a été spécifié, on initialise un dictionnaire vide de livres
        if books is None:
            self.books = {}
        # Sinon, on utilise le dictionnaire de livres donné
        else:
            self.books = books

    # Méthode pour embaucher un employé
    def hire_employee(self, employee):
        # On ajoute l'employé à la liste des employés de la bibliothèque
        self.employees.append(employee)

    # Méthode pour ajouter un livre à la bibliothèque
    def add_book(self, book):
        # Si le livre n'est pas déjà dans la bibliothèque, on l'ajoute avec un emprunteur vide
        if book not in self.books:
            self.books[book] = ""

        # Sinon, on affiche un message indiquant que le livre est déjà présent dans la bibliothèque
        else:
            print(f"{self.name} a déjà ce livre!")

    # Méthode pour emprunter un livre
    def borrow_book(self, book, borrower):
        # Si le livre est dans la bibliothèque, on met à jour l'emprunteur du livre
        print(self.books)
        if book in self.books:
            self.books[book] = borrower

            print(self.books)
        # Sinon, on affiche un message indiquant que le livre n'est pas disponible
        else:
            print(f"désolé, nous n'avons pas {book}.")

    # Méthode pour rendre un livre
    def return_book(self, book):
        # Si le livre est dans la bibliothèque, on met à jour l'emprunteur du livre pour indiquer qu'il est rendu
        if book in self.books:
            self.books[book] = ""
            # print("liste livre:",self.books)
        # Sinon, on affiche un message indiquant que le livre n'appartient pas à cette bibliothèque
        else:
            print("désolé, pas notre bibliothèque.")

    # Méthode pour afficher l'objet Library sous forme de chaîne de caractères
    def __str__(self):
        return self.name


#Le code vérifie d'abord si le script en cours d'exécution est le script principal en utilisant l'instruction if __name__ == "__main__":.
#Cela permet de s'assurer que le code ne sera exécuté que lorsque le script sera exécuté directement et non lorsqu'il sera importé par un autre script.
if __name__ == "__main__":
    # Création d'un objet Library avec le nom "Campel" et les listes et dictionnaires vides par défaut
    # pour les employés et les livres.
    library = Library("Campel", [], {})

    # Création de deux employés
    employee1 = {"id": 1, "name": "John"}
    employee2 = {"id": 2, "name": "Jane"}

    # Ajout des employés à la bibliothèque
    library.hire_employee(employee1)
    library.hire_employee(employee2)

    # Ajout de deux livres à la bibliothèque
    library.add_book("Lv01")
    library.add_book("Lv02")



    # Emprunt du livre Lv02 par Peter
    library.borrow_book("Lv02", "Peter")
    library.borrow_book("Lv02", "gegeg")

    # Rendu du livre Lv01
    library.return_book("Lv01")


# print(library)

