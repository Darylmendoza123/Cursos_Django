from django.shortcuts import render, HttpResponse

menu="""

<a href="/">principal</a>
<a href="/cursos">Cursos</a>
<a href="/contacto">Formulario de Inscripcion</a>
"""


# Create your views here.

def principal(request):
    return render(request,"contenido/principal.html")

def cursos(request):
    return render(request,"contenido/cursos.html")
   

def contacto(request):
    return render(request,"contenido/contacto.html")