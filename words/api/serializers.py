from datetime import timezone, datetime

from rest_framework import serializers
from ..models import Word, Theme


# Validators
def available_language(value):
    # language_list = list(Word.LANGUAGE.keys())
    language_list = ['en','es','it']
    # validation of available language
    print(value)
    if not (value in language_list):
        raise serializers.ValidationError("Language is not available")


# class WordSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     word = serializers.CharField(required=True)
#     language = serializers.CharField(required=True, validators= [available_language])
#     theme = serializers.CharField(required=True)
#     date_joined = serializers.DateField(default = datetime.today())
#
#     def create(self, validated_data):
#         return Word.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.word = validated_data.get('word', instance.word)
#         instance.language = validated_data.get('language', instance.language)
#         instance.theme = validated_data.get('theme', instance.theme)
#         instance.date_joined = validated_data.get('date_joined', instance.date_joined)
#         instance.save()
#         return instance
#
#     # Fields Validation
#
#     # Field-Level validation
#     # validate language field
#     # def validate_language(self,value):
#     #     # if the length of the language field is not 2, throw an exception
#     #     if len(value) != 2:
#     #         raise serializers.ValidationError('The length of the language field is not 2.')
#
#     # Object-Level validation
#     def validate(self, data):
#         # validation
#         if not ( str.isalpha(str(data['word']))  and  str.isalpha(str(data['theme']))):
#             raise serializers.ValidationError("The fields cannot contain numbers.")
#         return data


class WordSerializer(serializers.ModelSerializer):
    # custom serializer field
    size = serializers.SerializerMethodField()
    # override language field because need to implement validators


    class Meta:
        model = Word
        fields = "__all__"
        # exclude any fields
        # exclude = ['date_joined']

    def validate(self, data):
        # validation
        if not ( str.isalpha(str(data['word']))  and  str.isalpha(str(data['theme']))):
            raise serializers.ValidationError("The fields cannot contain numbers.")
        return data

    # custom serializer field method
    # structure  get_name_field
    def get_size(self,obj):
        return len(obj.word)



# class ThemeSerializer(serializers.ModelSerializer):
class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    wordlist = WordSerializer(many = True, read_only=True)
    # wordlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only= True,
    #     view_name= 'theme-details'
    # )
    language = serializers.CharField(required=True, validators=[available_language])
    class Meta:
        model = Theme
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'theme-details'}
        }