from rest_framework import serializers
from ..models  import Word

# # validate field language
# def validate_language(value):
#     # if language field is not String throw exception
#     if len(value) != 2 :
#         raise serializers.ValidationError('Language field is not String')


class WordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    word = serializers.CharField(required=True)
    language = serializers.CharField(required=True)
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