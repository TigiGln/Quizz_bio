from django.shortcuts import render
from .models import Images
from quizz.models import Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def data(request):
    images = Images.objects.all()
    data = {"images": images}
    return render(request, 'home/data.html', data)

def score(request):
    score = Profile.objects.all()
    #name = User.objects.all()
    data = {"score_user" : score}
    return render(request, 'home/score.html', data)