from django.http import HttpResponse
import datetime


def saludo(request):  # primera vista
    documento = """<html>
        <body>
            <h1>Hola, esta es mi primera página con django</h1>
        </body>
    </html>"""
    return HttpResponse(documento)


def despedida(request):  # segunda vista
    return HttpResponse("¡Hasta luego mundo!")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
        <body>
            <h2>Fecha y hora actuales %s</h2>
        </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, year):
    periodo = year - 2021
    edadFutura = edad + periodo

    documento = """<html>
        <body>
            <h2>En el año %s tendrás %s años</h2>
        </body>
    </html>""" % (year, edadFutura)

    return HttpResponse(documento)
