from django.db import models
from django.db.models.functions import Now

class Word(models.Model):
    LANGUAGE = {
        "en" : "English",
        "es" : "Spanish",
        "it" : "Italian"

    }
    word =  models.CharField(max_length=30)
    language =  models.CharField(max_length=2, choices = LANGUAGE)
    theme = models.CharField(max_length=30)
    date_joined = models.DateField(db_default= Now())

    # toString
    def __str__(self):
        return self.word

    # Metadata for Model
    class Meta:
        db_table = "words_table"
        db_table_comment = "Table for words"
        ordering = ["-date_joined"]
        verbose_name_plural = "words"


