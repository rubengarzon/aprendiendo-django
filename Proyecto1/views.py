from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):  # primera vista
    doc_externo = open(
        "C:/Users/ruben/Documents/estudios/django/Proyecto1/Proyecto1/plantillas/index.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
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
