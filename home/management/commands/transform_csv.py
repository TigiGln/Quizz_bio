#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:01:08 2021

@author: thierry
"""
import csv, json

def transform_csv_in_json(file):
    with open('../data/' + file, 'r') as file_csv:
        lines = file_csv.readlines()
        fieldnames = lines[0].strip().split(',')
        reader = csv.DictReader(lines[1:], fieldnames)
    with open('../data/' + file.split('.')[0] + '.json', 'w') as file_json:
        for row in reader:
            json.dump(row, file_json)
    print("votre fichier " + file_csv.name.split("/")[-1] + " a bien été converti en " + file_json.name.split("/")[-1] + "\n")

transform_csv_in_json("table_answers.csv")
transform_csv_in_json("table_question.csv")
transform_csv_in_json("tables_images.csv")
