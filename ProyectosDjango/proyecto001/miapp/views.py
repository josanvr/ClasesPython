from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request, 'saludo.html')

def rango(request):
    a = 10
    b= 20
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