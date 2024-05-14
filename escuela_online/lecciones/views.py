from django.shortcuts import render, get_object_or_404, redirect
from .models import Leccion
from .forms import LeccionForm

def lecciones_list(request):
    lecciones = Leccion.objects.all()
    return render(request, 'lecciones/lecciones_list.html', {'lecciones': lecciones})

def crear_lecciones(request):
    if request.method == 'POST':
        form = LeccionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lecciones_list')
    else:
        form = LeccionForm()
    return render(request, 'lecciones/crear_lecciones.html', {'form': form})

def detalle_lecciones(request, id):
    leccion = get_object_or_404(Leccion, pk=id)
    return render(request, 'lecciones/detalle_lecciones.html', {'leccion': leccion})

def editar_lecciones(request, id):
    leccion = get_object_or_404(Leccion, pk=id)
    if request.method == 'POST':
        form = LeccionForm(request.POST, request.FILES, instance=leccion)
        if form.is_valid():
            form.save()
            return redirect('lecciones_list')
    else:
        form = LeccionForm(instance=leccion)
    return render(request, 'lecciones/editar_lecciones.html', {'form': form})

def eliminar_lecciones(request, id):
    leccion = get_object_or_404(Leccion, pk=id)
    if request.method == 'POST':
        leccion.delete()
        return redirect('lecciones_list')
    return render(request, 'lecciones/eliminar_lecciones.html', {'leccion': leccion})
