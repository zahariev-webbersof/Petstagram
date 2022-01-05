from django.urls import path

from Petstagram.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]