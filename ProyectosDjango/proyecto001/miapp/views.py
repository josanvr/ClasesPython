from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    estudiantes = ['Carlos Ruiz','Jordy Quispe','Oscar Reyes','Antony Vasquez']
    #estudiantes = []
    return render(request, 'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web con Django en LP3',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos',
        'nombre_autor':'Jose Andres Vera Rodriguez'
    })


def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request, 'rango.html', {
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros': rango_numeros
    })

def rango2(request, a, b):
    if a>b:
        return redirect('rango2', a=b, b=a)
    resultado = f"""
             <h2> Numeros de [{a},{b}] </h2>
                  resultado: <br>
             <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado +="</ul>"
    return HttpResponse(resultado)