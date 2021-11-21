from django.shortcuts import render
from .models import Images
from quizz.models import Profile
from quizz.views import retrieve_score
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def index(request):
    """
    recovery of the score data of the connected user and creation of the site's home page

    :parameter:
        request: object request Http

    :return:
        the template chosen for the url
    """
    score = retrieve_score(request)
    context = {"score": score}
    return render(request, 'home/index.html', context)

def data(request):
    """
    managing the exploration of image data in the database

    :parameter:
        request: object request Http

    :return:
        the template chosen for the url
    """
    score = retrieve_score(request)
    images_list = Images.objects.all().values()
    list_images = []
    for elem in range(0, len(images_list)):
        list_images.append(images_list[elem])
    paginator = Paginator(images_list, 6)
    list_pages = []
    for pages in range(1, paginator.num_pages, 5):
        list_pages.append(pages)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver las page of results.
        images = paginator.page(paginator.num_pages)
    images_json = json.dumps(list_images, cls=DjangoJSONEncoder)
    data = {"images": images, 'paginate':True, "page_paginate": list_pages, "score":score, "my_data": images_json}
    return render(request, 'home/data.html', data)

def score(request):
    """
    management of the scoreboard for the users of the application

    :parameter:
        request: object request Http

    :return:
        the template chosen for the url
    """
    score_user = retrieve_score(request)
    score = Profile.objects.all()
    data = {"score_user" : score, "score": score_user}
    return render(request, 'home/score.html', data)