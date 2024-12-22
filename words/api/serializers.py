from rest_framework import serializers

class WordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    word = serializers.CharField()
    language = serializers.CharField()
    theme = serializers.CharField()
    date_joined = serializers.DateField()

