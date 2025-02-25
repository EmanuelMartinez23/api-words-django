from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import Theme_ListAV, Theme_DetailAV, LanguageList, LanguageDetail, WordList, WordDetail, ThemeList, \
    ThemeDetail, WordsByTheme, WordsByLanguage, WordsByThemeAndLanguage, LanguageVS, LanguageMVS
from ..api.views import word_list, word_details, word_listAV, word_detailsAV
# Only test viewset and routers
router = DefaultRouter()
router.register('languagesVS', LanguageVS, basename = 'languages')
router.register('languagesMVS', LanguageMVS, basename = 'languagesM')

urlpatterns = [
    # path('', word_list, name = "word-list" ),  # decorator @api_view()
    # path('<int:pk>', word_details, name = "word-details" ),

    # path('words/', word_listAV.as_view(), name = "word-list" ), # With APIView Class
    # path('words/<int:pk>', word_detailsAV.as_view(), name = "word-details" ),
    # path('themes/', Theme_ListAV.as_view(), name="theme-list"),  # With APIView Class
    # path('themes/<int:pk>', Theme_DetailAV.as_view(), name="theme-details"),

    # With Generic APIView
    path('words/', WordList.as_view(), name = "word-list" ),
    path('words/<int:pk>', WordDetail.as_view(), name = "word-details" ),
    path('themes/', ThemeList.as_view(), name = "theme-list" ),
    path('themes/<int:pk>', ThemeDetail.as_view(), name = "theme-detail" ),
    # With Mixins
    path('languages/', LanguageList.as_view(), name = "language-list" ),
    path('languages/<int:pk>', LanguageDetail.as_view(), name = "language-detail" ),
    # With Generic APIView
    path('themes/<int:pk>/words', WordsByTheme.as_view(), name = "Word-by-theme"),
    path('languages/<int:pk>/words', WordsByLanguage.as_view(), name = "Word-by-language"),
    path('themes/<int:pk>/languages/<int:pk2>/words', WordsByThemeAndLanguage.as_view(), name = "Word-by-language-theme"),
    # With Viewsets and Router,
    path('', include(router.urls)),
    # basic auth (temporary)
    path('api-auth', include('rest_framework.urls')),
    # path('account/', include('user_app.api.urls'))

]

