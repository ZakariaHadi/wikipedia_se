from rest_framework import serializers
from .models import Titre


class TitreSerializer(serializers.Serializer):
    class Meta:
        model = Titre
        fields = ['id','titre','taille','dateCreation']
