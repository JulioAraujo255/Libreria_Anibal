from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Autor, Genero, Libro, Calificacion
from .serializers import AutorSerializer, GeneroSerializer, LibroSerializer, CalificacionSerializer
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from .models import Libro
from .serializers import LibroSerializer



# libros/views.py
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def create(self, request, *args, **kwargs):
        # Detectamos si el body es una lista de objetos
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Si es solo un objeto
            return super().create(request, *args, **kwargs)
        
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Llamamos a la API de JWT (localmente)
        response = requests.post('http://127.0.0.1:8001/api/token/', data={
            'username': username,
            'password': password
        })

        if response.status_code == 200:
            tokens = response.json()
            access_token = tokens['access']
            refresh_token = tokens['refresh']
            # Guardamos el token en la sesión (como ejemplo)
            request.session['access_token'] = access_token
            return redirect('profile')  # redirige a una vista protegida
        else:
            error = 'Credenciales incorrectas'
    
    return render(request, 'login.html', {'error': error})

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email
        })
    
@api_view(['GET'])
def sugerencias_por_genero(request, genero_id):
    libros = Libro.objects.filter(
        genero=genero_id,
        calificacion__puntaje__gte=5  # Filtramos por calificación ≥ 5
    ).order_by('-calificacion__puntaje')
    
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data)
