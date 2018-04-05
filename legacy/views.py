from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import EmpresaContratante, Contratante, Musico, Produtor, Tecnico
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Count, Min, Sum, Avg
from .forms import EmpresaContratanteForm, ContratanteForm, MusicoForm, ProdutorForm, TecnicoForm
# Create your views here.


def home(request):

    return render(request, 'legacy/home.html', {})


# EMPRESA CONTRATANTES
def empresas(request):
    empresas = EmpresaContratante.objects.all()
    if request.POST:

        form = EmpresaContratanteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('empresas')
        context = {
            'empresas': empresas,
            'formempresas': form
        }

        return render(request, 'legacy/empresas.html', context)

    form = EmpresaContratanteForm()

    context = {
        'empresas': empresas,
        'formempresas': form
    }

    return render(request, 'legacy/empresas.html', context)


def empresaEdit(request, pk):

    q = get_object_or_404(EmpresaContratante, pk=pk)

    form = EmpresaContratanteForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('empresas')

    context = {
        'formempresaedit': form,
        'id': q.id
    }

    return render(request, 'legacy/empresa_edit.html', context)


def empresasDelete(request, pk):
    q = get_object_or_404(EmpresaContratante, pk=pk)
    q.delete()

    return redirect('empresas')


# CONTRATANTES PROMOTER
def contratante(request):
    contratantes = Contratante.objects.all()
    if request.POST:

        form = ContratanteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contratante')
        context = {
            'contratantes': contratantes,
            'formcontratante': form
        }

        return render(request, 'legacy/contratante.html', context)

    form = ContratanteForm()

    context = {
        'contratantes': contratantes,
        'formcontratante': form
    }

    return render(request, 'legacy/contratante.html', context)


def contratanteEdit(request, pk):

    q = get_object_or_404(Contratante, pk=pk)

    form = ContratanteForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('contratante')

    context = {
        'formcontratanteedit': form,
        'id': q.id
    }

    return render(request, 'legacy/contratante_edit.html', context)


def contratanteDelete(request, pk):
    q = get_object_or_404(Contratante, pk=pk)
    q.delete()

    return redirect('contratante')


# PRODUTOR
def produtor(request):
    produtores = Produtor.objects.all()
    if request.POST:

        form = ProdutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('produtor')
        context = {
            'produtores': produtores,
            'formprodutor': form
        }

        return render(request, 'legacy/produtor.html', context)

    form = ProdutorForm()

    context = {
        'produtores': produtores,
        'formprodutor': form
    }

    return render(request, 'legacy/produtor.html', context)


def produtorEdit(request, pk):

    q = get_object_or_404(Produtor, pk=pk)

    form = ProdutorForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('produtor')

    context = {
        'formprodutoredit': form,
        'id': q.id
    }

    return render(request, 'legacy/produtor_edit.html', context)


def produtorDelete(request, pk):
    q = get_object_or_404(Produtor, pk=pk)
    q.delete()

    return redirect('produtor')


# MUSICOS


def musico(request):
    musicos = Musico.objects.all()
    if request.POST:

        form = MusicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('musico')
        context = {
            'musicos': musicos,
            'formmusico': form
        }

        return render(request, 'legacy/musico.html', context)

    form = MusicoForm()

    context = {
        'musicos': musicos,
        'formmusico': form
    }

    return render(request, 'legacy/musico.html', context)


def musicoEdit(request, pk):

    q = get_object_or_404(Musico, pk=pk)

    form = MusicoForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('musico')

    context = {
        'formmusicoedit': form,
        'id': q.id
    }

    return render(request, 'legacy/musico_edit.html', context)


def musicoDelete(request, pk):
    q = get_object_or_404(Musico, pk=pk)
    q.delete()

    return redirect('musico')

# TECNICO


def tecnico(request):
    tecnicos = Tecnico.objects.all()
    if request.POST:

        form = TecnicoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tecnico')
        context = {
            'tecnicos': tecnicos,
            'formtecnico': form
        }

        return render(request, 'legacy/tecnico.html', context)

    form = TecnicoForm()

    context = {
        'tecnicos': tecnicos,
        'formtecnico': form
    }

    return render(request, 'legacy/tecnico.html', context)


def tecnicoEdit(request, pk):

    q = get_object_or_404(Tecnico, pk=pk)

    form = TecnicoForm(request.POST or None, instance=q)

    if form.is_valid():
        form.save()
        return redirect('tecnico')

    context = {
        'formtecnicoedit': form,
        'id': q.id
    }

    return render(request, 'legacy/tecnico_edit.html', context)


def tecnicoDelete(request, pk):
    q = get_object_or_404(Tecnico, pk=pk)
    q.delete()

    return redirect('tecnico')
