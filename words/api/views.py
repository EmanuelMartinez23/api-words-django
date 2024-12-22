from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializers import WordSerializer
from ..models import Word

@api_view(['GET'])
def word_list(request):
    words =  Word.objects.all()
    serializer  = WordSerializer(words, many=True)
    return Response(data=serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def word_details(request, pk):
    word = Word.objects.get(pk = pk)
    serializer = WordSerializer(word)
    return Response(data = serializer.data, status = HTTP_200_OK)