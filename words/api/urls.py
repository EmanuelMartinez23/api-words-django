from django.urls import path

from ..api.views import word_list, word_details

urlpatterns = [
    path('', word_list, name = "word-list" ),
    path('<int:pk>', word_details, name = "word-details" )
]