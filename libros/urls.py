
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, GeneroViewSet, LibroViewSet, CalificacionViewSet, login_view, ProfileView

# libros/urls.py
router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'calificaciones', CalificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    
]
