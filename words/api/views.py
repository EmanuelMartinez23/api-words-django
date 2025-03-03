from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, \
    HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import WordUserOrReadOnly
from .serializers import WordSerializer, ThemeSerializer, LanguageSerializer
from ..models import Word, Theme, Language

# views with decorator @api_view
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


# Views with Mixins, POST, GET
class LanguageList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # method get: use list method (documentation)
    def get(self,request, *args, **kwargs):
        return self.list(request, *args,**kwargs)

    # method post: use created method (documentation)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# View with mixins, GET, DELETE
class LanguageDetail(mixins.RetrieveModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # query_set = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_queryset(self):
        # obtain pk for record
        pk = self.kwargs['pk']
        return Language.objects.filter(pk = pk)

    def get(self, request, *args,**kwargs):
        return self.retrieve(request, *args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# Views con Generic Api View (Concrent View Class)
# POST, GET
class WordList(generics.ListCreateAPIView, generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['theme__theme', 'created_by__username', 'language__name']
    search_fields = ['^word']

    # for the user who has created a word
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# GET, PUT, DELETE
class WordDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # add custom permission
    permission_classes = [WordUserOrReadOnly]

# GET, POST
class ThemeList(generics.ListCreateAPIView, generics.GenericAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['children']
    search_fields = ['=theme']


class ThemeDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class WordsByTheme(generics.ListAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Word.objects.filter(theme = pk)

class WordsByLanguage(generics.ListAPIView):
    serializer_class = WordSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Word.objects.filter(language = pk)

class WordsByThemeAndLanguage(generics.ListAPIView):
    serializer_class = WordSerializer
    def get_queryset(self):
        theme = self.kwargs['pk']
        language = self.kwargs['pk2']
        return Word.objects.filter(theme = theme ).filter(language = language)

# View using ViewSets
class LanguageVS(viewsets.ViewSet):
    def list(self, request):
        queryset = Language.objects.all()
        serializer = LanguageSerializer(queryset,many = True)
        return Response(serializer.data)
    def retrieve(self, request, pk = None):
        queryset = Language.objects.all()
        language = get_object_or_404(queryset, pk = pk )
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def create(self,request):
        queryset = Language.objects.all()
        serializer = LanguageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# View using ModelViewSet  GET, POST, PUT, DELETE
class LanguageMVS(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer