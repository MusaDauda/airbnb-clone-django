from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversations Admin Definition"""

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Messages Admin Definition"""

    pass
