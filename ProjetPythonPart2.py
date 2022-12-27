class CarnetAdresse:
    def __init__(self, nom, contacts, livres):
        self.nom = nom
        self.contacts = contacts
        self.livres = livres

    def addContact(self, contact):
        f = open('./contacts.txt', 'a')
        print(type(contact))
        print(contact.__str__())
        # for contact in self.contacts:

        f.write(contact.__str__() + " -")

        f.close()

    def listContact(self):
        f = open('./contacts.txt', 'r')
        s_list = f.read().split("|")
        listeContact = ""

        for i in range(len(s_list)):
            if i % 2 != 0:
                print(s_list[i])
                listeContact += s_list[i] + "\n"

        f.close()
        return listeContact

    def printDetailsContact(self, contact):
        self.contact = contact
        f = open('./contacts.txt', 'r')
        s_list = f.read().split("-")
        contactExist = False
        details =""

        for n in range(len(s_list)):
            s_list2 = s_list[n].split(":")
            for i in range(len(s_list2)):
                if i % 2 != 0:
                    s_list3 = s_list2[i].split("|")
                    if s_list3[1] == " " + self.contact + " ":
                        contactExist = True
                        print(s_list[n])

                        details += s_list[n] + "\n"
        f.close()
        return details


    def supCon(self, contact):
        self.contact = contact
        f = open('./contacts.txt', 'r')
        dataFile = f.read().split("-")
        f.close()
        dataFile2 = dataFile.copy()

        for n in range(len(dataFile)):
            s_list2 = dataFile[n].split(":")
            for i in range(len(s_list2)):
                if i % 2 != 0:
                    s_list3 = s_list2[i].split("|")
                    if s_list3[1] == " " + self.contact + " ":
                        print(dataFile2)
                        print(n)
                        dataFile2.pop(n)
                        print("testttt", dataFile2)

        f = open('./contacts.txt', 'w')

        for contact in dataFile2:
            f.write(contact + " -")

        f.close()

    def modCon(self, contact, newId, newNom):
        self.contact = contact
        self.id = newId
        self.nom = newNom
        f = open('./contacts.txt', 'r')
        dataFile = f.read().split("-")
        f.close()
        dataFile2 = dataFile.copy()
        # self.supCon(self.contact)

        for n in range(len(dataFile)):
            s_list2 = dataFile[n].split(":")
            for i in range(len(s_list2)):
                if i % 2 != 0:
                    s_list3 = s_list2[i].split("|")
                    if s_list3[1] == " " + self.contact + " ":
                        print('modification en cour...')
                        print(self.contact)
                        self.supCon(self.contact)
                        f = open('./contacts.txt', 'r')
                        dataFile3 = f.read().split("-")
                        print("file3", dataFile3)
                        con1 = Contact(self.id, self.nom)
                        print("pr:", dataFile2)
                        dataFile3.append(con1.__str__())
                        print('modification reussi')

        f = open('./contacts.txt', 'w')

        for contact in dataFile3:
            f.write(contact + " -")

        f.close()

    def clearContacts(self):
        f=open('./contacts.txt', 'w')
        f.write("")
        f.close()


class Contact:
    def __init__(self, nom, mail):
        self.mail = mail
        self.nom = "| " + nom + " |"


    def __str__(self):
        return f" {self.mail} : {self.nom}"


