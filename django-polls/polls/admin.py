"""
Django admin configuration for the Polls app.

This module defines the admin interface for the Polls app, including
the Question and Choice models.
"""

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """
    Inline admin interface for Choice model.

    This class defines the inline presentation of Choice models within the
    Question admin interface.
    """
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Question model.

    This class defines the admin interface for the Question model. It
    includes fieldsets, inlines, list display, filters, and search fields.
    """
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]



admin.site.register(Question, QuestionAdmin)
