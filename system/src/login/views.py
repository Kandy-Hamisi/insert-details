from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel
from .forms import MyForm
# Create your views here.

def my_form(request):
    
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form  = MyForm()
    return render(request, 'login.html', {'form': form})