from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIFFICULTY_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
OPTION_CHOICES = [('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')]


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    number_of_questions = models.IntegerField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    score = models.IntegerField()

class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES)