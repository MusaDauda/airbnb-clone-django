from django.contrib import admin
from lists import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Definition"""

    pass
