from django.shortcuts import render
from django import forms
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import io, base64

class MetodoForm(forms.Form):
    funcion = forms.CharField(label='Función polinómica', max_length=100)
    metodo = forms.ChoiceField(choices=[
        ('biseccion', 'Bisección'),
        ('newton', 'Newton-Raphson'),
        ('newton_mod', 'Newton-Raphson Modificado')
    ])
    a = forms.FloatField(required=False, label='a (solo para Bisección)')
    b = forms.FloatField(required=False, label='b (solo para Bisección)')
    x0 = forms.FloatField(required=False, label='x0 (para Newton y Newton Modificado)')
    tolerancia = forms.FloatField(label='Tolerancia')
    max_iter = forms.IntegerField(label='Máximo número de iteraciones')

def index(request):
    resultado, grafico = None, None
    if request.method == 'POST':
        form = MetodoForm(request.POST)
        if form.is_valid():
            f_str = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            x0 = form.cleaned_data.get('x0')
            tol = form.cleaned_data['tolerancia']
            n = form.cleaned_data['max_iter']
            x = sp.symbols('x')
            try:
                f_expr = sp.sympify(f_str)
                f = sp.lambdify(x, f_expr, 'numpy')
                df = sp.lambdify(x, sp.diff(f_expr, x), 'numpy')
                iteraciones = []
                if metodo == 'biseccion':
                    if a is None or b is None:
                        raise ValueError("Debe ingresar a y b para Bisección")
                    if f(a) * f(b) >= 0:
                        raise ValueError("No hay cambio de signo en [a,b]")
                    for i in range(1, n+1):
                        c = (a + b) / 2
                        fc = f(c)
                        error = abs(b - a)
                        iteraciones.append((i, a, b, c, fc, error))
                        if error < tol or abs(fc) < tol:
                            break
                        if f(a) * fc < 0:
                            b = c
                        else:
                            a = c
                    raiz = c
                elif metodo == 'newton':
                    if x0 is None:
                        raise ValueError("Debe ingresar x0 para Newton-Raphson")
                    xi = x0
                    for i in range(1, n+1):
                        dfx = df(xi)
                        if dfx == 0:
                            raise ZeroDivisionError("Derivada cero en iteración")
                        xi1 = xi - f(xi)/dfx
                        error = abs(xi1 - xi)
                        iteraciones.append((i, xi, xi1, f(xi), dfx, error))
                        if error < tol:
                            break
                        xi = xi1
                    raiz = xi1
                elif metodo == 'newton_mod':
                    if x0 is None:
                        raise ValueError("Debe ingresar x0 para Newton-Raphson Modificado")
                    xi = x0
                    dfx0 = df(xi)
                    if dfx0 == 0:
                        raise ZeroDivisionError("Derivada inicial cero")
                    for i in range(1, n+1):
                        xi1 = xi - f(xi)/dfx0
                        error = abs(xi1 - xi)
                        iteraciones.append((i, xi, xi1, f(xi), dfx0, error))
                        if error < tol:
                            break
                        xi = xi1
                    raiz = xi1
                xs = np.linspace(-10, 10, 400)
                ys = f(xs)
                plt.figure()
                plt.axhline(0, color='gray')
                plt.plot(xs, ys, label=str(f_expr))
                plt.scatter([raiz], [f(raiz)], color='red')
                plt.title("Gráfico del polinomio")
                plt.legend()
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()
                grafico = base64.b64encode(image_png).decode('utf-8')
                resultado = {'iteraciones': iteraciones, 'raiz': raiz}
            except Exception as e:
                resultado = {'error': str(e)}
    else:
        form = MetodoForm()
    return render(request, 'calculadora/index.html', {'form': form, 'resultado': resultado, 'grafico': grafico})
