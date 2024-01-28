from django.shortcuts import render, redirect
from .models import Atricles
from .forms import AtriclesForm


def n(request):
    nn = Atricles.objects.order_by('-date')
    return render(request, 'tablica/asdf.html', {'nn': nn})


def create(request):
    error = ''
    if request.method == 'POST':
        form = AtriclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tablica')
        else:
            error = 'text'

    form = AtriclesForm()

    date = {
        'form': form,
        'error': error
    }

    return render(request, 'tablica/create.html', date)
