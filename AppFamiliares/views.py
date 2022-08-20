from django.shortcuts import render
from django.template import loader
from AppFamiliares.models import Familiar
from django.http import HttpResponse

# Create your views here.
def listaFamiliares (self):
    padre=Familiar (nombre="Eduardo", apellido="Vergini",edad= 63, direccion="Santiago del Estero 536", tel= 1543077881, email="vergini@tandar.cnea.gov.ar", relacion="Papá", cumpleaños="1959-10-01")
    padre.save()
    madre= Familiar(nombre="Judith", apellido="Rodriguez", edad= 58, direccion= "Santiago del Estero 536", tel=1553329367, email="jrodriguez@gmil.com", relacion="Mamá", cumpleaños="1964-08-12")
    madre.save()
    abuelo=Familiar(nombre="Horacio",apellido="Rodríguez",edad= 92, direccion="Anchorena 1245",tel= 1568547895, email="hrodriguez@gmail.com",relacion="Abuelo", cumpleaños="1930-12-22")
    abuelo.save()
    hermana=Familiar(nombre="Julieta",apellido="Vergini",edad= 35, direccion="Decatur St. SE 25, Atlanta",tel=1587596875, email="rosebudck@gmail.com",relacion="Hermana", cumpleaños="1987-09-03")
    hermana.save()
    prima=Familiar(nombre="Stefanía",apellido="Vergini",edad= 30, direccion="Donizetti 548",tel= 1589637521, email="svergini@gmail.com",relacion="Prima", cumpleaños="1992-02-20")


    diccionario={"padre":padre,"madre":madre,"abuelo":abuelo,"hermana":hermana, "prima":prima}

    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

