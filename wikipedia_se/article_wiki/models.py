from django.db import models
from titre_wiki.models import Titre
import uuid

class Article(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.CharField(max_length=100)
    corps = models.CharField(max_length=1000)
    dateCreation = models.TimeField(auto_now=True)

    def __str__(self):
        return self.corps
