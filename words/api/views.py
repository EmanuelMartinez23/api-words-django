
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, \
    HTTP_404_NOT_FOUND
from .serializers import WordSerializer
from ..models import Word

@api_view(['GET', 'POST'])
def word_list(request):
    if request.method == 'GET':
        words =  Word.objects.all()
        serializer  = WordSerializer(words, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    if request.method == 'POST':
        serializer = WordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors,status = HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def word_details(request, pk):
    if request.method == 'GET':
        try:
            word = Word.objects.get(pk = pk)
        except Word.DoesNotExist:
            return Response(
                "{ error : Word not found }",
                status=HTTP_404_NOT_FOUND)

        serializer = WordSerializer(word)
        return Response(data = serializer.data, status = HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            word = Word.objects.get(pk = pk)
        except Word.DoesNotExist:
            return Response(
                "{error : Word not found }",
                status = HTTP_404_NOT_FOUND
            )

        word.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        try:
            word = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response("{ error : Word not found }", status = HTTP_404_NOT_FOUND)

        serializer =  WordSerializer(instance=word , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = HTTP_200_OK)
        else:
            return Response(data = serializer.errors, status =  HTTP_400_BAD_REQUEST)
