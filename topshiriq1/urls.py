from django.contrib import admin
from django.urls import path
from project.views import online_dokon
urlpatterns = [
    path('admin/', admin.site.urls),
    path('online_shop/',online_dokon),
]
