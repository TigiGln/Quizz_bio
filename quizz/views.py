from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ParagraphErrorList
from django.db import transaction, IntegrityError
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your views here.
def index(request):
    return HttpResponse("Ceci est un quizz")

def register(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST, error_class=ParagraphErrorList)
        context={'form':form}
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                with transaction.atomic():
                    user = User.objects.filter(email=email)
                    if not user.exists():
                        #If user is not registered, create a new one
                        new_user=User.objects.create(
                            username=name,
                            email=email,
                            password = PBKDF2PasswordHasher(password)
                        )
                    new_profile = Profile.objects.create(
                        user= user.first(),
                        score = 0
                    )
                    return render(request, 'registration/login.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."          
    else:
        form = UserForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'registration/register.html', context)
    