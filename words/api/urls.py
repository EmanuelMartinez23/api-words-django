from django.urls import path

from ..api.views import word_list, word_details, word_listAV, word_detailsAV

urlpatterns = [
    # path('', word_list, name = "word-list" ),  # decorator @api_view()
    # path('<int:pk>', word_details, name = "word-details" ),
    path('', word_listAV.as_view(), name = "word-list" ), # With APIView Class
    path('<int:pk>', word_detailsAV.as_view(), name = "word-details" )
]
