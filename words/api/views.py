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

class LanguageList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    View to list and create languages
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LanguageDetail(mixins.RetrieveModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    """
    View to retrieve, update and delete a language
    """
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
    """
    View to list and create words
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['theme__theme', 'created_by__username', 'language__name']
    search_fields = ['^word']

    # for the user who has created a word
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class WordDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    """
    View to retrieve, update and delete a word
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # add custom permission
    permission_classes = [WordUserOrReadOnly]

class ThemeList(generics.ListCreateAPIView, generics.GenericAPIView):
    """
    View to list and create themes
    """
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['children']
    search_fields = ['=theme']

class ThemeDetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
    """
    View to retrieve, update and delete a theme
    """
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class WordsByTheme(generics.ListAPIView):
    """
    View to list words by theme
    """
    serializer_class = WordSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Word.objects.filter(theme = pk)

class WordsByLanguage(generics.ListAPIView):
    """
    View to list words by languages
    """
    serializer_class = WordSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Word.objects.filter(language = pk)

class WordsByThemeAndLanguage(generics.ListAPIView):
    """
    View to list words by theme and language
    """
    serializer_class = WordSerializer
    def get_queryset(self):
        theme = self.kwargs['pk']
        language = self.kwargs['pk2']
        return Word.objects.filter(theme = theme ).filter(language = language)
