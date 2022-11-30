# NYC Guide

### This project is a coordinated effort by Amanda Testerman and Christopher Cialone

## Description
This project is structured as a guide to the Boros of New York City, where each boro has different activities, and the activities have different venues. All of our data is actually housed in one giant nested dictionary in the settings.py file. The structure is what is important in this particular project.

## Developers, open a new terminal...

1. **First Off** go to wherever you keep your content and make a django-projects directory there. You'll use this directory to store your apps and practice code.

2. **Then** clone the repo

3. **Now** Locate nyc-guide-main and cd into it

4. **Next** Run your computer's version of python3 -m venv venv to create a new virtual environment (it's common practice to name your virtual environment 'venv')

5. **Run** source venv/bin/activate on Unix/MacOS or venv\Scripts\activate.bat on Windows to activate the virtual environment

6. **Next** Run pip install django to install Django

7. **Run** pip freeze > requirements.txt (take a look at the new requirements file that popped up!) NOTE: this 'freezes' all of the libraries/frameworks required to make the project work as expected at their current version, so that you can easily download the requirements on a different computer.

8. ##And now## From your virtual environment run $ python3 manage.py runserver

9. Hover over Starting development server at http://127.0.0.1:8000/ and hold command and click with the mouse, which will take you to the guide! 

10. Click on the links to explore

