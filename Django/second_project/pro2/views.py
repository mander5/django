from django.http import HttpResponse
from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'pro2/index.html')

def help(request):
    my_dict = {'helpline':"Help Page"}
    return render(request, 'pro2/help.html', context=my_dict)

def signup(request):
    form = forms.NewUserForm()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error form invalid')

    return render(request, 'pro2/sign-up.html', {'form':form})
