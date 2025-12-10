from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro
from .forms import CarroForm

# LISTAR CARROS
def listar(request):
    carros = Carro.objects.all()
    return render(request, 'listar.html', {'carros': carros})

# CRIAR CARRO
def criar(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar')
    else:
        form = CarroForm()
    return render(request, 'criar.html', {'form': form})

# EDITAR CARRO
def editar(request, id):
    carro = get_object_or_404(Carro, id=id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'editar.html', {'form': form})

# DELETAR CARRO
def deletar(request, id):
    carro = get_object_or_404(Carro, id=id)
    carro.delete()
    return redirect('listar')
