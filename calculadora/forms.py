from django import forms

METODOS = [
    ('biseccion', 'Bisección'),
    ('newton', 'Newton-Raphson'),
    ('newton_mod', 'Newton-Raphson Modificado'),
]

class MetodoForm(forms.Form):
    funcion = forms.CharField(
        label="Función polinómica",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: x**3 - x - 2'})
    )
    metodo = forms.ChoiceField(
        label="Método",
        choices=METODOS
    )
    a = forms.FloatField(
        required=False,
        label="Límite inferior (a)",
        widget=forms.NumberInput(attrs={'placeholder': 'Ej: 1.0'})
    )
    b = forms.FloatField(
        required=False,
        label="Límite superior (b)",
        widget=forms.NumberInput(attrs={'placeholder': 'Ej: 2.0'})
    )
    x0 = forms.FloatField(
        required=False,
        label="Valor inicial (x₀)",
        widget=forms.NumberInput(attrs={'placeholder': 'Ej: 1.5'})
    )
    tolerancia = forms.FloatField(
        label="Tolerancia",
        initial=1e-5,
        widget=forms.NumberInput(attrs={'step': 'any'})
    )
    max_iteraciones = forms.IntegerField(
        label="Máximo número de iteraciones",
        initial=100,
        min_value=1
    )
