from django.urls import path

from .views import Theme_ListAV, Theme_DetailAV, LanguageList, LanguageDetail
from ..api.views import word_list, word_details, word_listAV, word_detailsAV

urlpatterns = [
    # path('', word_list, name = "word-list" ),  # decorator @api_view()
    # path('<int:pk>', word_details, name = "word-details" ),
    path('words/', word_listAV.as_view(), name = "word-list" ), # With APIView Class
    path('themes/', Theme_ListAV.as_view(), name = "theme-list" ), # With APIView Class
    path('themes/<int:pk>', Theme_DetailAV.as_view(), name = "theme-details" ),
    path('words/<int:pk>', word_detailsAV.as_view(), name = "word-details" ),
    # With Mixins
    path('languages/', LanguageList.as_view(), name = "language-list" ),
    path('languages/<int:pk>', LanguageDetail.as_view(), name = "language-detail" ),

]
