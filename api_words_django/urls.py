
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('words.api.urls')),
    path('', include('user_app.api.urls'))
]
