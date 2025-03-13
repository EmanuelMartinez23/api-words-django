from django.contrib.auth.models import User
from django.db import models

class Language(models.Model):
    """
    Model representing a language.
    """
    name = models.CharField(max_length= 100, unique=True)
    code = models.CharField(max_length=10, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.code} "

class Theme(models.Model):
    """
    Model representing a theme for words.
    """
    theme = models.CharField(max_length=30, default='Unknown')
    children = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.theme

class Word(models.Model):
    """
    Model representing a word in a specific language and theme.
    """
    word =  models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add= True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="wordlist")
    language = models.ForeignKey(Language, on_delete = models.CASCADE, related_name= "language_word")

    def __str__(self):
        return self.word

    class Meta:
        db_table = "words_table"
        ordering = ["-date_joined"]
        verbose_name_plural = "words"


