from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Question, Answers
from home.models import Images
from .forms import UserForm, ParagraphErrorList
from django.db import transaction, IntegrityError
import random


# Create your views here.
def retrieve_score(request):
    """
    recovery of the user's score for all pages of the site after login

    :parameter:
        request: object request Http

    :return:
        score: int
            user's score
    """
    score=""
    if request.user.is_authenticated:
        score = Profile.objects.get(user=request.user)
    return score
    

def register(request):
    """
    function to manage the user registration interface and to create a score profile for each user in the database

    :parameter:
        request: object request Http

    :return:
        returns to the home page if the user is correctly registered. 
        If not, it stays on the registration page and displays the errors 
    """
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST, error_class=ParagraphErrorList)
        context={'form':form}
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                #transactions allow you to cancel all the queries executed if there is an error before the end
                with transaction.atomic():
                    user = User.objects.filter(email=email)
                    if not user.exists():
                        #If user is not registered, create a new one
                        new_user=User.objects.create_user(
                            username=name,
                            email=email,
                            password = password
                        )
                    new_profile = Profile.objects.create(
                        user= user.first(),
                        score = 0
                    )
                    context["register"] = "Well registered user"
                    return render(request, 'home/index.html', context)
            except IntegrityError:
                form.errors['internal'] = "An internal error has occurred. Please try your request again."          
    else:
        form = UserForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'registration/register.html', context)

def choice_quizz(request):
    """
    function to manage the different possible quizzes

    :parameter:
        request: object request Http

    :return:
        return the block allowing to choose the quiz 
    """
    score = retrieve_score(request)
    questions = Question.objects.all()
    list_category = []
    for question in questions:
        list_category.append(question.category)
    list_category.insert(1, "mixed")
    data = {'list_category':list_category, "score": score}
    return render(request, "quizz/choice_quizz.html", data)

def score_change(request, response, answer, question_points):
    """
    function to update the user's score according to their answers to the quiz

    :parameter:
        request: object request Http
        response: str
            response given by the user
        answer: str
            correct answer to the question
        question_points: int
            the number of points for the question

    :return:
        None
        Updating the Profile Table with the new score 
    """
    score_user = Profile.objects.get(user=request.user).score
    if str(response) == str(answer):
        new_score = score_user + int(question_points)
        
    else:
        new_score = score_user - int(question_points)
        if new_score < 0:
            new_score = 0
    Profile.objects.filter(user=request.user).update(score = new_score)


def quizz(request):
    """
    Function to generate the quiz chosen by the user 

    :parameter:
        request: object request Http

    :return:
        The template according to the chosen quiz 
    """
    mode = request.GET.get('choice_quizz')
    context = {}
    if(request.method == "POST"):
        response = request.POST.get('answer')
        answer = request.POST.get('answer_preview')
        question_points = request.POST.get('question_points')
        score_change(request, response, answer, question_points)
    if mode == "microscopy" or mode == "component" or mode == "mixed":
        if mode == "mixed":
            index = random.randint(1, 2)
            question = Question.objects.get(question_id=index)
            question_points = 2
            context["question_points"] = question_points
        else:
            question = Question.objects.get(category__icontains = mode)
            question_points=question.points
            context["question_points"] = question_points
        context["question"] = question
        answers = Answers.objects.filter(question = question.question_id)
        context["answers"] = answers
        random_answer = random.sample(list(answers), 1)
        answer = random_answer[0].answer
        context['random'] = answer
        if question.category == "microscopy":
            images = Images.objects.filter(microscopy__icontains = answer)
        elif question.category == "component":
            images = Images.objects.filter(component__icontains = answer)
        random_images = random.sample(list(images), question.nb_image)
        context["images"] = random_images
        context['random'] = answer
    else:
        context["error"] = "The mode you have chosen does not exist in this quiz"
    score = retrieve_score(request)
    context["score"] = score
    return render(request, 'quizz/quizz.html', context)

    