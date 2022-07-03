from django.contrib import admin
from . import models

# from users.models import User
# admin.site.register(User)


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
