from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, esta es mi primera vista en Django!")
# Create your views here.
def mi_vistaroja(request):
    return HttpResponse("<p style='color: blue;'>¡Hola, esta es mi primera vista en Django!</p>")