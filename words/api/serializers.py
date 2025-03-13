from datetime import timezone, datetime

from rest_framework import serializers
from ..models import Word, Theme, Language

# Validators
def available_language(value):
    language_list = ['en','es','it']
    print(value)
    if not (value in language_list):
        raise serializers.ValidationError("Language is not available")

class WordSerializer(serializers.ModelSerializer):
    """
    Serializer for Word model.
    """
    size = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField(read_only = True)
    theme = serializers.StringRelatedField(read_only =True)
    language = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Word
        fields = "__all__"

    def get_size(self,obj):
        return len(obj.word)

class LanguageSerializer(serializers.ModelSerializer):
    """
    Serializer for Language model.
    """
    class Meta:
        model = Language
        fields = "__all__"

# class ThemeSerializer(serializers.ModelSerializer):
class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    wordlist = WordSerializer(many = True, read_only=True)
    language_word = LanguageSerializer(many = True, read_only =True)

    class Meta:
        model = Theme
        fields = "__all__"
