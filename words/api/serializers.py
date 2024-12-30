from datetime import timezone, datetime

from rest_framework import serializers
from ..models  import Word

# Validators
def available_language(value):
    # language_list = list(Word.LANGUAGE.keys())
    language_list = ['en','es','it']
    # validation of available language
    print(value)
    if not (value in language_list):
        raise serializers.ValidationError("Language is not available")


class WordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    word = serializers.CharField(required=True)
    language = serializers.CharField(required=True, validators= [available_language])
    theme = serializers.CharField(required=True)
    date_joined = serializers.DateField()

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.word = validated_data.get('word', instance.word)
        instance.language = validated_data.get('language', instance.language)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.save()
        return instance

    # Fields Validation

    # Field-Level validation
    # validate language field
    # def validate_language(self,value):
    #     # if the length of the language field is not 2, throw an exception
    #     if len(value) != 2:
    #         raise serializers.ValidationError('The length of the language field is not 2.')

    # Object-Level validation
    def validate(self, data):
        # validation
        if not ( str.isalpha(str(data['word']))  and  str.isalpha(str(data['theme']))):
            raise serializers.ValidationError("The fields cannot contain numbers.")
        return data

