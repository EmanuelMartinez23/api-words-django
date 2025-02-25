from datetime import timezone, datetime

from rest_framework import serializers
from ..models import Word, Theme, Language


# Validators
def available_language(value):
    # language_list = list(Word.LANGUAGE.keys())
    language_list = ['en','es','it']
    # validation of available language
    print(value)
    if not (value in language_list):
        raise serializers.ValidationError("Language is not available")

class WordSerializer(serializers.ModelSerializer):
    # custom serializer field
    size = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField(read_only = True)
    # override language field because need to implement validators
    class Meta:
        model = Word
        fields = "__all__"

    # custom serializer field method
    # structure  get_name_field
    def get_size(self,obj):
        return len(obj.word)



# Serializer for Language
class LanguageSerializer(serializers.ModelSerializer):
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
        # extra_kwargs = {
        #     'url': {'view_name': 'theme-details'}
        # }
