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

3. Make little migrations as possible when defining your app models.

#### When importing modules, a good practice is to...
1. Import python and django modules first at the top.
2. Import Third Party modules preceding the top modules
3. Finally, import your modules at the bottom of the stack order.

#### When defining foreign keys or importing, some good practice and tweaks.....
1. Define your import using strings => `""`
```python
class Photo(core_models.TimeStampedModel):
    """Photo Model Definition."""

    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=CASCADE)

# This will have an error if `Room` is not defined first before before the Photo class. A good practice is...


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition."""

    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=CASCADE)

    ## Yes, enclose in quotes, haha...

# If you do this correctly, you might not have to import every model you create or need.
# I still like importing though 🚶
```

#### def _str(self): function (self-depr method.... forgive me🤣):
```python
class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created ## Django is expecting a string, it gets a DateTime object(Hence Error).
        #return str(self.created) ## Here we force a string conversion


        # I will be getting back to that though, just to hack it for now...


```