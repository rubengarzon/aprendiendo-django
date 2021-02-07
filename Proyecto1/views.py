from django.http import HttpResponse


def saludo(request):  # primera vista
    return HttpResponse("Hola, esta es mi primera página con django")


def despedida(request):  # segunda vista
    return HttpResponse("¡Hasta luego mundo!")
