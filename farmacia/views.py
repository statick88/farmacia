from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicamento
from .forms import MedicamentoForm

def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'farmacia/lista_medicamentos.html', {'medicamentos': medicamentos})

def detalle_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    return render(request, 'farmacia/detalle_medicamento.html', {'medicamento': medicamento})

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'farmacia/crear_medicamento.html', {'form': form})

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'farmacia/editar_medicamento.html', {'form': form})

def eliminar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    medicamento.delete()
    return redirect('lista_medicamentos')

