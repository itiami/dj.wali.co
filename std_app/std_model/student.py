

class Student:

    # Le Constructeur de le Class
    def __init__(self, nom ="", prenom ="", phone =""):
        self.nom = nom
        self.prenom = prenom
        self.phone = phone

    def __repr__(self):
        return (
            
                "Nom: " +self.nom +
                ", Prenom: " + self.prenom+
                ", Phone: " + self.phone
            
        )


    # Le getter de le Class
    def get_nom(self):
        return self.nom

    # Le getter de le Class
    def set_nom(self, nom):
        self.nom = nom

    # Le getter de le Class
    def get_prenom(self):
        return self.prenom

    # Le getter de le Class
    def set_prenom(self, prenom):
        self.prenom = prenom
    
    # Le getter de le Class
    def get_phone(self):
        return self.phone

    # Le getter de le Class
    def set_phone(self, phone):
        self.phone = phone

    