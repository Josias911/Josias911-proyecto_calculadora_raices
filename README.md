
# 🧮 Calculadora de Raíces de Polinomios

Este proyecto es una aplicación web desarrollada con Django que permite calcular raíces de funciones polinómicas utilizando métodos numéricos como:

- Método de Bisección
- Método de Newton-Raphson
- Método de Newton-Raphson Modificado

Incluye visualización de resultados, iteraciones y gráficos generados automáticamente.

---

## 🚀 Características

- Interfaz amigable para el usuario.
- Ingreso dinámico de funciones polinómicas.
- Soporte para diferentes métodos de búsqueda de raíces.
- Visualización de tabla de iteraciones y gráficos del polinomio.

---

## 🛠️ Requisitos

- Python 3.10 o superior
- pip
- Virtualenv (opcional pero recomendado)

---

## 📦 Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/Josias911/Josias911-proyecto_calculadora_raices.git
cd Josias911-proyecto_calculadora_raices
```

2. **Crea un entorno virtual (opcional):**

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución del servidor

```bash
python manage.py runserver
```

Abre tu navegador y entra a:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Métodos Implementados

### 1. Bisección
Requiere un intervalo `[a, b]` donde la función cambie de signo.

### 2. Newton-Raphson
Requiere un valor inicial `x₀` y evalúa derivadas de la función.

### 3. Newton-Raphson Modificado
Similar al anterior pero con optimización en el cálculo de derivadas.

---

## 📁 Estructura del proyecto

```
proyecto_calculadora_raices/
│
├── calculadora/           # Aplicación principal
│   ├── templates/
│   └── views.py
├── proyecto_calculadora_raices/
│   └── settings.py
├── static/
├── manage.py
└── README.md
```
