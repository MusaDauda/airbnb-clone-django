# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more ... 🐍

## Creating Django Projects
Start project with:
```
django-admin startproject config
```
Rename root config folder(This is to avoid naming conflict when moving inner config folder), move inner config folder and ``manage.py`` file to root and delete old config folder.

## Creating Django Apps
1. _Never have to many functionalities in one app_
   ***Divide and Conquer***

    ##### Rule of thump for creating Django Applications
            You should be able to describe the application in one sentence
        
   
2. Applications name should be **plurals.** A good example is  posts, users, todos etc.