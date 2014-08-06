from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from meibos.models import Meibo, Gendar, Busyo

class MeiboForm(forms.ModelForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Meibo 

def index(request):
    data = {'meibo': Meibo.objects.all()}
    return render(request, 'index.html', data)

def new(request):
    form = MeiboForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('index')
    return render(request, 'detail.html', {'form':form})

def detail(request, pk):
    meibo = get_object_or_404(Meibo, id=pk)
    form = MeiboForm(request.POST or None, instance=meibo)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'detail.html', {'form':form, 'id':pk})

def delete(request, pk):
    meibo = get_object_or_404(Meibo, id=pk)    
    if request.method=='POST':
        meibo.delete()
        return redirect('index')
    return render(request, 'delete.html')

