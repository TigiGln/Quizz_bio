import os
import logging as lg

import csv
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from home.models import Images

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
                if(table == "Images"):
                    try:
                        stored_image = Images.objects.get(image_name = dico['image_name'])
                        lg.info("L'image est déjà inclut dans la base de données")
                    except ObjectDoesNotExist:
                        image = Images.objects.create(
                            image_id = dico['image_id'],
                            image_name = dico['image_name'],
                            description = dico['description'],
                            microscopy = dico['microscopy'],
                            cell_type = dico['cell_type'],
                            component = dico['component'],
                            doi = dico['doi'],
                            organism = dico['organism']
                        )
                        lg.info("L'image a bien été ajoutée")
                            
            
            
            
        