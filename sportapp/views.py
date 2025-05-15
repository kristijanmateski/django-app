from django.shortcuts import render, redirect, get_object_or_404

from sportapp.forms import SupplementForm
from sportapp.models import Supplement


# Create your views here.


def index(request):
    category = request.GET.get('category')
    if category:
        supplements = Supplement.objects.filter(category=category)
    else:
        supplements = Supplement.objects.all()

    return render(request, 'index.html', {'supplements': supplements})


def add(request):
    if request.method == 'POST':
        form = SupplementForm(request.POST, request.FILES)
        if form.is_valid():
            supplement = form.save(commit=False)
            supplement.image = form.cleaned_data['image']
            supplement.save()
            return redirect('index')
    return render(request, 'add.html', {'form': SupplementForm()})


def details(request, pk):
    supplement = Supplement.objects.get(id=pk)
    context = {'supplement': supplement}
    return render(request, 'detail.html', context=context)


def delete(request, pk):
    supplement = Supplement.objects.filter(id=pk).get()
    if request.method == 'POST':
        supplement.delete()
        return redirect('index')
    else:
        return redirect('index')


def edit(request, pk):
    supplement = get_object_or_404(Supplement, pk=pk)
    if request.method == 'POST':
        form = SupplementForm(request.POST, request.FILES, instance=supplement)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SupplementForm(instance=supplement)

    return render(request, 'edit.html', {'form': form})
