from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente, Horario, Doctor, Agenda, SignoVital
from .forms import PacienteForm, HorarioForm, DoctorForm, AgendaForm, SignoVitalForm
from django.http.response import HttpResponseForbidden 
from django.contrib import messages

# Vista de Inicio


class InicioView(TemplateView):
    template_name = "index.html"

# Vista de Pacientes
#    Lista los registros de los pacientes

# PACIENTE
class PacienteView(ListView):
    model = Paciente
    template_name = "base/paciente/paciente.html"
    context_object_name = "pacientes"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 5

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de pacientes"
        return context

#    Crea un nuevo registro de los pacientes


class CrearPacienteView(CreateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"
#    Edita o modifica  un registro de los pacientes


class EditarPacienteView(UpdateView):
    model = Paciente
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/paciente/registrar_paciente.html"
    form_class = PacienteForm
    success_url = reverse_lazy('base:paciente')
    context_object_name = "pacientes"


class EliminarPacienteView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            paciente = Paciente.objects.get(id=pk)
            paciente.delete()
            # object.estado = False
            # object.save()
            return redirect('base:paciente')
        except:
            messages.error(request,'NO ES POSIBLE ELIMINAR ESTE DATO')
            return redirect('base:paciente')

# HORARIO
class ListadoHorarioView(ListView):
    model= Horario
    template_name = "base/horario/listar_horario.html"
    context_object_name='horarios'

class CrearHorarioView(CreateView):
    model = Horario
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')
    context_object_name = "horarios"
#    Edita o modifica  un registro de los pacientes

class EditarHorarioView(UpdateView):
    model = Horario
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/horario/registrar_horario.html"
    form_class = HorarioForm
    success_url = reverse_lazy('base:horario')
    context_object_name = "horarios"


class EliminarHorarioView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            horario = Horario.objects.get(id=pk)
            horario.delete()
            # object.estado = False
            # object.save()
            return redirect('base:horario')
        except:
            messages.error(request,'NO ES POSIBLE ELIMINAR ESTE DATO') 
            return redirect('base:horario')

# DOCTOR
class DoctorView(ListView):
    model = Doctor
    template_name = "base/doctor/doctor.html"
    context_object_name = "doctores"
    #queryset = Paciente.objects.filter(estado=False)
    paginate_by = 5

    def get_queryset(self):
        nombre = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        return self.model.objects.filter(nombre__icontains=nombre, estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get(
            'nombre') if self.request.GET.get('nombre') else ''
        context['titulo'] = "Consulta de doctores"
        return context

#    Crea un nuevo registro de los pacientes


class CrearDoctorView(CreateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/registrar_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctores"
#    Edita o modifica  un registro de los pacientes


class EditarDoctorView(UpdateView):
    model = Doctor
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/doctor/registrar_doctor.html"
    form_class = DoctorForm
    success_url = reverse_lazy('base:doctor')
    context_object_name = "doctores"


class EliminarDoctorView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            doctor = Doctor.objects.get(id=pk)
            doctor.delete()
            # object.estado = False
            # object.save()
            return redirect('base:doctor')
        except:
            messages.error(request,'NO ES POSIBLE ELIMINAR ESTE DATO')
            return redirect('base:doctor')

# CITAS
class ListadoCitaView(ListView):
    model= Agenda
    template_name = "base/cita/listar_cita.html"
    context_object_name='agendas'

class CrearCitaView(CreateView):
    model = Agenda
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/cita/registrar_cita.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:cita')
    context_object_name = "agendas"
#    Edita o modifica  un registro de los pacientes

class EditarCitaView(UpdateView):
    model = Agenda
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/cita/registrar_cita.html"
    form_class = AgendaForm
    success_url = reverse_lazy('base:cita')
    context_object_name = "agendas"


class EliminarCitaView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            agenda = Agenda.objects.get(id=pk)
            agenda.delete()
            # object.estado = False
            # object.save()
            return redirect('base:cita')
        except:
            messages.error(request,'NO ES POSIBLE ELIMINAR ESTE DATO')
            return redirect('base:cita')

# SIGNO VITALES
class ListadoSigVitalView(ListView):
    model= SignoVital
    template_name = "base/signoVital/signoVital.html"
    context_object_name='signoVitales'

class CrearSigVitalView(CreateView):
    model = SignoVital
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signoVital/registrar_signoVital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:signoVital')
    context_object_name = "signoVitales"
#    Edita o modifica  un registro de los pacientes

class EditarSigVitalView(UpdateView):
    model = SignoVital
    #fields = ['nombre', 'apellido', 'cedula']
    template_name = "base/signoVital/registrar_signoVital.html"
    form_class = SignoVitalForm
    success_url = reverse_lazy('base:signoVital')
    context_object_name = "signoVitales"

class EliminarSigVitalView(DeleteView):

    def post(self, request, *args, **kwargs):
        try:
            pk = request.POST.get("id")
            sigVital = SignoVital.objects.get(id=pk)
            sigVital.delete()
            # object.estado = False
            # object.save()
            return redirect('base:signoVital')
        except:
            messages.error(request,'NO ES POSIBLE ELIMINAR ESTE DATO')
            return redirect('base:signoVital')