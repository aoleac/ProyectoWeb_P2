from django.urls import path
from .views import *
app_name = 'base'
urlpatterns = [
#PACIENTE
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('editar_paciente/<int:pk>/',
         EditarPacienteView.as_view(), name='editar_paciente'),
    path('eliminar_paciente/<int:pk>/',
         EliminarPacienteView.as_view(), name='eliminar_paciente'),
#DOCTOR
    path('doctor/', DoctorView.as_view(), name='doctor'),
    path('registrar_doctor/', CrearDoctorView.as_view(), name='registrar_doctor'),
    path('editar_doctor/<int:pk>/',
         EditarDoctorView.as_view(), name='editar_doctor'),
    path('eliminar_doctor/<int:pk>/',
         EliminarDoctorView.as_view(), name='eliminar_doctor'),
#HORARIO
    path('horario/',ListadoHorarioView.as_view(), name='horario'),
    path('registrar_horario/', CrearHorarioView.as_view(),name='registrar_horario'),
    path('eliminar_horario/<int:pk>/', EliminarHorarioView.as_view(),name='eliminar_horario'),
    path('editar_horario/<int:pk>/', EditarHorarioView.as_view(),name='editar_horario'),
#CITAS
    path('cita/',ListadoCitaView.as_view(), name='cita'),
    path('registrar_cita/', CrearCitaView.as_view(),name='registrar_cita'),
    path('eliminar_cita/<int:pk>/', EliminarCitaView.as_view(),name='eliminar_cita'),
    path('editar_cita/<int:pk>/', EditarCitaView.as_view(),name='editar_cita'),
#SIGNO VITAL
    path('signoVital/',ListadoSigVitalView.as_view(), name='signoVital'),
    path('registrar_signoVital/', CrearSigVitalView.as_view(),name='registrar_signoVital'),
    path('eliminar_signoVital/<int:pk>/', EliminarSigVitalView.as_view(),name='eliminar_signoVital'),
    path('editar_signoVital/<int:pk>/', EditarSigVitalView.as_view(),name='editar_signoVital'),
]
