"""
Django models for the Question and Choice classes.
"""

import datetime
from django.contrib import admin

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Represents a question.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        """
        Check if the question was published recently.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    """
    Represents a choice for a question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
