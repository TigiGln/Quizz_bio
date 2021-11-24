![Python 3.8.5](https://img.shields.io/badge/Python-3.8.5-blue.svg)
![PyPI - Django Version](https://img.shields.io/badge/django-3.7.2-orange.svg)

# M2 DLAD Django Project

## Biological Quiz

* This project aims to implement a web interface illustrating 
the functionalities of the Django framework through an organic quiz
* The programming language used is Django, using python, HTML and JavaScript.
* The result will be displayed in a web browser page



## Web application

Web application
* The application has different functionalities:
    - The exploration of the biological content of the database 
    - A score table to track our score against other registered users
    - A registration system for new users
    - A login system to access the quiz
    - a biological quiz in three modes: microscopy, components and mixe
    
    
### Dependencies 

* The application therefore uses Django to create this web interface. 
To install Django with the latest stable version:
```{}
sudo apt install python-django
```
ou
```{}
sudo pip3 install django
```
* To start a Django project:
```{}
django-admin startproject <nameproject>
```
* To start the project database:
```{}
python3 manage.py migrate
```
* To create a application
```{}
python manage.py startapp <nameapp>
```
* To start the server:
```{}
python manage.py runserver
```

To populate the databases, one can find overloads of manage.py:
```{}
python manage.py add_images tables_images.csv
python manage.py add_bdd table_answers.csv
python manage.py add_bdd table_question.csv
```



## Launch project

```{}
git clone https://github.com/TigiGln/Quizz_bio.git
cd <project>
python manage.py runserver
```
* Open a web browser and type in the address:

http://127.0.0.1:8000/


#### You can now browse the application to create an account and take the quizzes or explore the biological data.

