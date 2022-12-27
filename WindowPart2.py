import tkinter as tk


from ProjetPythonPart2 import CarnetAdresse, Contact


class App:
    def __init__(self, master):
        self.master = master
        self.carnet = CarnetAdresse("mon carnet", [], [])

        self.ClearButton = tk.Button(self.master, text="Clear Contacts", command=self.clear_Contacts)

        # Création de widgets pour ajouter un contact
        self.labelId = tk.Label(self.master, text="Nom et Prénom:" )
        self.entryId = tk.Entry(self.master)
        self.labelNom = tk.Label(self.master, text="Mail:")
        self.entryNom = tk.Entry(self.master)
        self.buttonAdd = tk.Button(self.master, text="Ajouter", command=self.add_contact)

        # Création de widgets pour lister les contacts
        self.buttonList = tk.Button(self.master, text="Lister", command=self.list_contacts)

        # Création de widgets pour afficher les détails d'un contact
        self.labelContact = tk.Label(self.master, text="Contact:")
        self.entryContact = tk.Entry(self.master)
        self.buttonDetails = tk.Button(self.master, text="Détails", command=self.print_details_contact)

        # Création de widgets pour supprimer un contact
        self.labelContactSup = tk.Label(self.master, text="Contact:")
        self.entryContactSup = tk.Entry(self.master)
        self.buttonSup = tk.Button(self.master, text="Supprimer", command=self.sup_con)

        # Création de widgets pour modifier un contact
        self.labelContactMod = tk.Label(self.master, text="Contact:")
        self.entryContactMod = tk.Entry(self.master)
        self.labelIdMod = tk.Label(self.master, text="Nom et Prénom:")
        self.entryIdMod = tk.Entry(self.master)
        self.labelNomMod = tk.Label(self.master, text="Mail:")
        self.entryNomMod = tk.Entry(self.master)
        self.buttonMod = tk.Button(self.master, text="Modifier", command=self.mod_con)

        # Placement des widgets dans la fenêtre
        self.labelId.grid(row=0, column=0)
        self.entryId.grid(row=0, column=1)
        self.labelNom.grid(row=0, column=2)
        self.entryNom.grid(row=0, column=3)
        self.buttonAdd.grid(row=0, column=4)
        self.buttonList.grid(row=1, column=0)
        self.labelContact.grid(row=2, column=0)
        self.entryContact.grid(row=2, column=1)
        self.buttonDetails.grid(row=2, column=2)
        self.labelContactSup.grid(row=3, column=0)
        self.entryContactSup.grid(row=3, column=1)
        self.buttonSup.grid(row=3, column=2)
        self.labelContactMod.grid(row=4, column=0)
        self.entryContactMod.grid(row=4, column=1)
        self.labelIdMod.grid(row=4, column=2)
        self.entryIdMod.grid(row=4, column=3)
        self.labelNomMod.grid(row=4, column=4)
        self.entryNomMod.grid(row=4, column=5)
        self.buttonMod.grid(row=4, column=6)
        self.labelDetails = tk.Label(self.master, text="")
        self.labelDetails.grid(row=3, column=3)
        self.ClearButton.grid(row=3, column=4)

    def clear_Contacts(self):
        self.carnet.clearContacts()

    def add_contact(self):
        # Récupération de l'ID et du nom entrés par l'utilisateur
        id = self.entryId.get()
        nom = self.entryNom.get()
        # Création d'un nouveau contact
        contact = Contact(id, nom)
        # Ajout du contact au carnet d'adresses
        self.carnet.addContact(contact)
        # Remise à vide des champs d'entrée
        self.entryId.delete(0, "end")
        self.entryNom.delete(0, "end")

    def list_contacts(self):
        # Appel de la méthode listContact() de la classe CarnetAdresse
        listeContact = self.carnet.listContact()

        self.labelDetails.configure(text=listeContact)



    def print_details_contact(self):
        # Récupération du nom du contact entré par l'utilisateur
        nom = self.entryContact.get()
        # Appel de la méthode printDetailsContact() de la classe CarnetAdresse
        details = self.carnet.printDetailsContact(nom)
        # Mise à jour du label avec les détails du contact
        self.labelDetails.configure(text=details)
        self.entryContact.delete(0, "end")


    def sup_con(self):
        # Récupération du nom du contact entré par l'utilisateur
        nom = self.entryContactSup.get()
        # Appel de la méthode supCon() de la classe CarnetAdresse
        self.carnet.supCon(nom)
        self.entryContactSup.delete(0, "end")


    def mod_con(self):
        # Récupération du nom du contact, de l'ID et du nom entrés par l'utilisateur
        nom = self.entryContactMod.get()
        id = self.entryIdMod.get()
        nom_mod = self.entryNomMod.get()
        # Appel de la méthode modCon() de la classe CarnetAdresse
        self.carnet.modCon(nom, id, nom_mod)
        self.entryContactMod.delete(0, "end")
        self.entryIdMod.delete(0, "end")
        self.entryNomMod.delete(0, "end")








# Création de la fenêtre principale
root = tk.Tk()
root.title("Le carnet de monsieur paul")
app = App(root)
root.mainloop()





# lib = CarnetAdresse("Campel", {}, {})
#
# con2 = Contact("2", "toi")
# con3 = Contact("3", "moi")
# con4 = Contact("4", "gonni")
# con5 = Contact("5", "dylan")
# con6 = Contact("6", "bernard")
# # CarnetAdresse("Campel", [con1.__str__(), con2.__str__(),con3.__str__(), con4.__str__(),con5.__str__(), con6.__str__()], {}).addContact()
# # lib.listContact()
# # lib.printDetailsContact('bernard')
# # lib.supCon('lui')
# # lib.modCon('toi',44,'toi2')
#
# # Création de la fenêtre principale
# fenetre = tk.Tk()
# fenetre.title("Le carnet de contact de Mr Paul")
#
#
# # Affichage de la fenêtre
# fenetre.mainloop()