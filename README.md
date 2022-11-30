# NYC Guide

### This project is a coordinated effort by Amanda Testerman and Christopher Cialone

## Description
This project is structured as a guide to the Boros of New York City, where each boro has different activities, and the activities have different venues. All of our data is actually housed in one giant nested dictionary in the settings.py file. The structure is what is important in this particular project.

## Developers, open a new terminal...

**First Off** go to wherever you keep your content and make a django-projects directory there. You'll use this directory to store your apps and practice code.

**Then** In the django-projects folder:

**Now** Create a new folder called nyc-guide-main and cd into it

**Next** Run your computer's version of python3 -m venv venv to create a new virtual environment (it's common practice to name your virtual environment 'venv')

**Run** source venv/bin/activate on Unix/MacOS or venv\Scripts\activate.bat on Windows to activate the virtual environment

**Next** Run pip install django to install Django

**Run** pip freeze > requirements.txt (take a look at the new requirements file that popped up!) NOTE: this 'freezes' all of the libraries/frameworks required to make the project work as expected at their current version, so that you can easily download the requirements on a different computer.

**Initialize your git instance** In your terminal, initialize a new instance of git with git init. Be sure to add and commit your progress as you go!

**Start a new Django project** with the command $ django-admin startproject mysite
$ ls
mysite/

**Then** navigate into the project folder you just created
$ cd mysite
$ ls
manage.py*  mysite/

**Now you can** run the Django server. Use the manage.py file to run the server! Don't worry about the "unapplied migrations" for now
$ python manage.py runserver
Go to localhost:8000 and you should see the Django welcome screen!
**Create your app** Use the manage.py file to start up your new app! Then inspect the files that are created.
$ python manage.py startapp nyc
$ ls
db.sqlite3  manage.py*  nyc/ mysite/
**Register your nyc app with the nyc-guide-main project**
Edit the mysite/settings.py 
INSTALLED_APPS = [
    'nyc.apps.NycConfig',
    ... # Leave all the other INSTALLED_APPS
]

