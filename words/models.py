from django.db import models
from django.db.models.functions import Now

class Language(models.Model):
    name = models.CharField(max_length= 100, unique=True)
    code = models.CharField(max_length=10, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.code} "


class Theme(models.Model):
    theme = models.CharField(max_length=30, default='Unknown')
    children = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.theme


class Word(models.Model):
    word =  models.CharField(max_length=30)
    # date_joined = models.DateField(db_default= Now())
    date_joined = models.DateTimeField(auto_now_add= True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="wordlist")
    language = models.ForeignKey(Language, on_delete = models.CASCADE, related_name= "language_word")

    # toString
    def __str__(self):
        return self.word

    # Metadata for Model
    class Meta:
        db_table = "words_table"
        ordering = ["-date_joined"]
        verbose_name_plural = "words"


