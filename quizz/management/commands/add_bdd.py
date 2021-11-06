import os
import logging as lg

import csv
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from quizz.models import Question, Answers

lg.basicConfig(level=lg.DEBUG)

class Command(BaseCommand):
    help = 'Add datas to the database from a csv file located in data/'

    def add_arguments(self, parser):
       parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        reference = 0
        #open file with data
        directory = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(directory, 'data', options['file'])
        with open(path, 'r') as file:
            table = file.name.split('_')[-1].split('.')[0].capitalize()
            lines = file.readlines()
            fieldnames = lines[0].strip().split(',')
            reader = csv.DictReader(lines[1:], fieldnames)
            for dico in reader:
                if (table == "Answers"):
                    try:
                        stored_answer = Answers.objects.get(answer = dico['answer'])
                        lg.info("La réponse est déjà inclut dans la base de données")
                    except ObjectDoesNotExist:
                        id_question = Question.objects.filter(question_id = dico['question_id'])
                        if id_question.exists():
                            answer = Answers.objects.create(
                                answer_id = dico['answer_id'],
                                question = id_question.first(),
                                answer = dico['answer'],
                                definition = dico['definition']
                            )
                            lg.info('La réponse à été créée')
                elif (table == "Question"):
                    try:
                        stored_question = Question.objects.get(question_id = dico['question_id'])
                        lg.info("La question est déjà inclut dans la base de données")
                    except ObjectDoesNotExist:
                        question = Question.objects.create(
                            question_id = dico['question_id'],
                            question = dico['question'],
                            category = dico['category'],
                            imageField = dico['imageField'],
                            points = dico['points'],
                            nb_answer = dico['nb_answer'],
                            nb_image = dico['nb_image'],
                        )
                        lg.info("La question a bien été ajoutée")