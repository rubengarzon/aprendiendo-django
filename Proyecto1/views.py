from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):  # primera vista
    p1 = Persona("Profesor Juan", "Díaz")
    temasDelCurso = ["Tema 1", "Tema 2", "Tema 3", "Tema 4", "Tema 5"]
    """ nombre = "Juan" """
    """ apellido = "García" """
    ahora = datetime.datetime.now()
    # doc_externo = open(
    #    "C:/Users/ruben/Documents/estudios/django/Proyecto1/Proyecto1/templates/index.html")
    #plantilla = Template(doc_externo.read())
    # doc_externo.close()

    doc_externo = get_template('index.html')

    # contexto = Context(
    #    {"nombre": p1.nombre, "apellido": p1.apellido, "momento_actual": ahora, "temas": temasDelCurso})
    documento = doc_externo.render(
        {"nombre": p1.nombre, "apellido": p1.apellido, "momento_actual": ahora, "temas": temasDelCurso})
    return HttpResponse(documento)


def despedida(request):  # segunda vista
    return HttpResponse("¡Hasta luego mundo!")


def dame_Fecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
        <body>
            <h2>Fecha y hora actuales %s</h2>
        </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)


def calcular_Edad(request, edad, year):
    periodo = year - 2021
    edadFutura = edad + periodo

    documento = """<html>
        <body>
            <h2>En el año %s tendrás %s años</h2>
        </body>
    </html>""" % (year, edadFutura)

    return HttpResponse(documento)
