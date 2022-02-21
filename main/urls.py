from django.urls import path, include

from main.views import ShowPost

urlpatterns = [
    path('', ShowPost.as_view(), name='home')
]