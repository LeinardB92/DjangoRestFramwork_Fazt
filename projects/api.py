from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# Qué consultas se podrán hacer, es dicir, sobre que datos se podrá hacer alguna consulta.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    # Cualquier cliente o aplicación cliente podrá solicitar datos al servidor, más adelante puedes cambiarlo por 'IsAuthenticated' para que solo de acceso a los autentificados 
    permission_classes = [permissions.AllowAny]

    # A partir de que serializer se va serializar el queryset, es decir, cómo lo se va a convertir.
    serializer_class = ProjectSerializer

# Hasta aquí ya terminamos nuestra API, pero hace falta una URL que el cliente pueda consultar.
