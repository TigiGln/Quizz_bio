from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    imageField = models.CharField(max_length=400)
    points = models.IntegerField()
    nb_answer = models.IntegerField()
    nb_image = models.IntegerField()

class Answers(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    definition = models.TextField()

class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField()