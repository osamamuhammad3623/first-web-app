from django.shortcuts import render
from .forms import customPasswordForm
from .models import password
import random 

# Create your views here.

def generate(request):
    passForm = customPasswordForm()
    generatedPass = ''
    if request.GET.get('generate') == 'Generate password!':

        # password generation logic
        cap_letters = 'ABCDEFGHIKJLMNOPQRSTVWXYZ'
        small_letters = cap_letters.lower()
        numbers = '0123456789'
        syms = '!.@#$%^&*()_+<>?|\/'
        chosen_types = ''

        if request.GET.get('letters') == 'clicked': chosen_types += cap_letters + small_letters
        if request.GET.get('numbers') == 'clicked': chosen_types += numbers
        if request.GET.get('symbols') == 'clicked': chosen_types += syms
        pass_length = int(request.GET.get('passLength'))

        first_char = random.choice(cap_letters + small_letters)
        rest_char = "".join(random.sample(chosen_types,pass_length -1))
        generatedPass = first_char + rest_char

        if request.POST.get('store') == 'store':
            password.objects.create(genPass = generatedPass, user = request.user)

        context={
            'generatedPass': generatedPass,
            'title':'CPG'
        }
        return render(request, 'passgen/generate.html', context=context)   

    return render(request, 'passgen/generate.html', context={'form': passForm, 'title':'CPG'})

def home(request):
    return render(request, 'passgen/home.html', context={'title':'Home'})