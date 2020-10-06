from django import forms
from django.db.models import fields
from .models import Paciente, Horario, Doctor, Agenda, SignoVital

# PACIENTE
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sangre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hijos': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

# HORARIO
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'dia': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholeder': 'Dia Semana'
                }
            ),
            'desde': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hasta': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

# DOCTOR
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'civil': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'profesion': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'titulo': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'consultorio': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'lugar': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'logo': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'horario': forms.SelectMultiple(
                attrs={
                    'class':'form-control'
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'duracion': forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

# CITAS
class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

# HORARIO
class SignoVitalForm(forms.ModelForm):
    class Meta:
        model = SignoVital
        # fields = ('nombre', 'apellido', 'cedula')
        # label = {
        #     'nombre': 'Nombres',
        #     'apellido': 'Apellidos',
        #     'cedula': 'Cedula'
        # }
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rango1': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rango2': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medida': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }