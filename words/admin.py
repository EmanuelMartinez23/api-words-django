from django.contrib import admin

from .models import Word, Theme, Language

# Register your models here.
admin.site.register(Word)
admin.site.register(Theme)
admin.site.register(Language)