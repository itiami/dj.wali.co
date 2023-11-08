from django.db import models


class StudentModel(models.Model):

    nom = models.CharField(max_length=70, blank=False, default="")
    prenom = models.CharField(max_length=70, blank=False, default="")
    phone = models.CharField(max_length=11, blank=False, default="")
    email = models.CharField(max_length=70, blank=False, default="")
    tarifRepas = models.CharField(max_length=4, blank=False)


# # Le Constructeur de le Class
# def __init__(self, nom="", prenom="", phone="", email=""):
#     self.nom = nom
#     self.prenom = prenom
#     self.phone = phone
#     self.email = email

# def __repr__(self):
#     return (

#         "Nom: " + self.nom +
#         ", Prenom: " + self.prenom +
#         ", Phone: " + self.phone +
#         ", Email: " + self.email

#     )

# # Le getter de le Class

# def get_nom(self):
#     return self.nom

# # Le getter de le Class
# def set_nom(self, nom):
#     self.nom = nom

# # Le getter de le Class
# def get_prenom(self):
#     return self.prenom

# # Le getter de le Class
# def set_prenom(self, prenom):
#     self.prenom = prenom

# # Le getter de le Class
# def get_phone(self):
#     return self.phone

# # Le getter de le Class
# def set_phone(self, phone):
#     self.phone = phone

# def get_email(self):
#     return self.email

# def set_email(self, email):
#     self.email = email
