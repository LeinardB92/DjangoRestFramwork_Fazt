from rest_framework import serializers
from .models import Project

# Esto convertirá un modelo en datos que pueden ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        # Nombre del modelo al que hacemos referencia.
        model = Project
        # Colocamos los campos que puedan ser consultados, es decir, que serán serializados.
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # Definimos que campos son solo de lectura, es decir que no podrán ser modificados.
        read_only_fields = ('created_at') 