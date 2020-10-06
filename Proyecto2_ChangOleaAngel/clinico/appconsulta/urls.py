from django.urls import path
from .views import *

app_name = "atencion"
urlpatterns = [
    path('historia/', HistoriaView2.as_view(), name='historia'),
    #RECETA
    path('recetas/', RecetasPacientes.as_view(), name='recetas'),
    path('registrar_receta/', NuevaRecetaPacientes.as_view(), name='registrar_receta'),
    #DETALLE RECETA
    path('registrar_detReceta/',DetalleRecetaPacientes.as_view(), name='registrar_detReceta'),
    path('detReceta/',DetalleRecetas.as_view(), name='detReceta'),
    #SIGNO VITAL
    path('toSigno/',SignosPacientes.as_view(), name='toSigno'),
    path('registrar_toSigno/',TomaSignosPacientes.as_view(), name='registrar_toSigno')
]
