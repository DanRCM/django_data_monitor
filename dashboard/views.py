from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Creamos un diccionario llamado 'data'
    # La clave 'title' será el nombre de la variable en el HTML
    data = {
        'title': "Landing Page Dashboard",
    }

    # Pasamos 'data' como tercer argumento a render
    return render(request, 'dashboard/index.html', data)