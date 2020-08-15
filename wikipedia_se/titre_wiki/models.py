from django.db import models

from .Titre_ES_Script import TitreIndex
# Create your models here.

class Titre(models.Model):
    titre = models.CharField(max_length=100)
    taille = models.IntegerField()
    dateCreation = models.TimeField(auto_now=True)

    def __str__(self):
        return self.titre


    # Methode qui décrit les specifications d'indexation du modele
    def indexing(self):
        objet = TitreIndex(
            meta={'id': self.id},
            titre=self.titre,
        )
        objet.save()
        return objet.to_dict(include_meta=True)