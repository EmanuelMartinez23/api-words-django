from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import  LanguageList, LanguageDetail, WordList, WordDetail, ThemeList, \
    ThemeDetail, WordsByTheme, WordsByLanguage, WordsByThemeAndLanguage

urlpatterns = [
    path('words/', WordList.as_view(), name = "word-list" ),
    path('words/<int:pk>', WordDetail.as_view(), name = "word-details" ),
    path('themes/', ThemeList.as_view(), name = "theme-list" ),
    path('themes/<int:pk>', ThemeDetail.as_view(), name = "theme-detail" ),
    path('languages/', LanguageList.as_view(), name = "language-list" ),
    path('languages/<int:pk>', LanguageDetail.as_view(), name = "language-detail" ),
    path('themes/<int:pk>/words', WordsByTheme.as_view(), name = "Word-by-theme"),
    path('languages/<int:pk>/words', WordsByLanguage.as_view(), name = "Word-by-language"),
    path('themes/<int:pk>/languages/<int:pk2>/words', WordsByThemeAndLanguage.as_view(), name = "Word-by-language-theme"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

