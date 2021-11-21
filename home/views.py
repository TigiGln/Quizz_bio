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

def search(request_search, fields):
    images_list = {}
    if "microscopy" in fields:
        images_list = Images.objects.filter(microscopy__icontains = request_search).values()
    elif "component" in fields:
        images_list = Images.objects.filter(component__icontains = request_search).values()
    elif "organism" in fields:
        images_list = Images.objects.filter(organism__icontains = request_search).values()
    return images_list

def data(request):
    """
    managing the exploration of image data in the database

    :parameter:
        request: object request Http

    :return:
        the template chosen for the url
    """
    score = retrieve_score(request)
    list_field = ["microscopy", "component", "organism"]
    list_images = []
    request_search = ""
    data = ""
    if request.method == "POST":
        request_search = request.POST.get('search')
        fields = request.POST.get("field")
        error=""
        if fields != "":
            images_list = search(request_search, fields)
            if images_list == {}:
                error = "There are no results for your search"
            else:
                for elem in range(0, len(images_list)):
                    list_images.append(images_list[elem])
        else:
            error = "You have not checked a radio button"
        images_json = json.dumps(list_images, cls=DjangoJSONEncoder)
        data = {"images":images_list, "score": score, "my_data": images_json, "list_field": list_field, "errors": error}
    else:
        images_list = Images.objects.all().values()

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
            #If page is out of range (e.g. 9999), deliver last page of results.
            images = paginator.page(paginator.num_pages)
        images_json = json.dumps(list_images, cls=DjangoJSONEncoder)
        data = {"images": images, 'paginate':True, "page_paginate": list_pages, "score":score, "my_data": images_json, "list_field": list_field}
        
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