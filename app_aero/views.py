from django.shortcuts import render

# Create your views here.
def index(request):
        empleados = [
        {'nombre': 'Alice Smith', 'puesto': 'Desarrollador Senior', 'salario': 75000},
        {'nombre': 'Bob Johnson', 'puesto': 'Diseñador UI/UX', 'salario': 60000},
        {'nombre': 'Charlie Brown', 'puesto': 'Gerente de Proyectos', 'salario': 85000},
    ]
        context = {
        'empleados': empleados
    }
        return render(request, 'index.html', context)