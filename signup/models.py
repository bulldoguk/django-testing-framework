from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from typing import Optional


class Question(models.Model):
    question_text: models.CharField = models.CharField(max_length=200)
    pub_date: models.DateTimeField = models.DateTimeField("date published")


def create_question(question_text: str) -> Question:
    qs: Question = Question(question_text=question_text, pub_date=timezone.now())
    qs.save()
    return qs


def get_question(question_text: str) -> Optional[Question]:
    return Question.objects.filter(question_text=question_text).first()


def filter_question(text: str) -> QuerySet[Question]:
    return Question.objects.filter(question_text___startswith=text)


class Choice(models.Model):
    question: models.ForeignKey = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: models.CharField = models.CharField(max_length=200)
    votes: models.IntegerField = models.IntegerField(default=0)
