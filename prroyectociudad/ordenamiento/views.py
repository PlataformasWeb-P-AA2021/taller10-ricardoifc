from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

# Create your views here.

def index(request):
    """
        Parroquias y barrios listados y obtenidos de la base de datos.
    """

    parroquias = Parroquia.objects.all()

    informacion_template = {'parroquias': parroquias}
    return render(request, 'index.html', informacion_template)


def to_list_parroquia(request):

    parroquia = Parroquia.objects.all()

    informacion_template = {'parroquia': parroquia}
    return render(request, 'to_list_parroquia.html', informacion_template)

def to_list_barrio(request):

    barrio = Barrio.objects.all()

    informacion_template = {'barrio': barrio}
    return render(request, 'to_list_barrio.html', informacion_template)

def add_parroquia(request):

    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'add_parroquia.html', diccionario) 

def add_barrio(request):

    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'add_barrio.html', diccionario) 

def edit_parroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'edit_parroquia.html', diccionario)

def edit_barrio(request, id):

    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'edit_barrio.html', diccionario) 

