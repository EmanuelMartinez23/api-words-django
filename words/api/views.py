from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, \
    HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from .serializers import WordSerializer, ThemeSerializer
from ..models import Word, Theme


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


# Views with APIView Class
class word_listAV(APIView):

    def get(self,request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self,request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

class word_detailsAV(APIView):
    def get(self,request,pk):
        try:
            word = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response(
                "{ error : Word not found }",
                status=HTTP_404_NOT_FOUND)

        serializer = WordSerializer(word)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self,request, pk):
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

    def delete(self, request,pk):
        try:
            word = Word.objects.get(pk = pk)
        except Word.DoesNotExist:
            return Response(
                "{error : Word not found }",
                status = HTTP_404_NOT_FOUND
            )

        word.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# # Views with APIView
class Theme_ListAV(APIView):
    def get(self, request):
        themes =  Theme.objects.all()
        serializer = ThemeSerializer(themes, many = True,  context={'request': request})
        return Response(data =serializer.data)

    def post(self,request):
        serializer = ThemeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors, status = HTTP_400_BAD_REQUEST)


class Theme_DetailAV(APIView):
    def get(self,request, pk):
        theme = Theme.objects.get(pk = pk)
        serializer = ThemeSerializer(theme, context={'request': request})
        return Response(serializer.data, status = HTTP_200_OK)

    def delete(self,request, pk):
        theme = Theme.objects.get(pk = pk)
        theme.delete()
        return  Response(status = HTTP_200_OK)

    def put(self, request, pk):
        theme = Theme.objects.get(pk = pk)
        serializer = ThemeSerializer(theme, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)